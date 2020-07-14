# module importation
import numpy as np
from python.finite_volume.helper import thermo, split
from python.boundary.boundary_cond import enforce_bc, covariant
from python.finite_volume.timestepping import local_timestep
import python.finite_volume.soln_vars as soln_vars
import python.finite_volume.flux as flux
import python.finite_volume.muscl as muscl
from pytictoc import TicToc

# Roe scheme
# see Ren, Gu, Li "New Roe Scheme For All Speed Flow" (2011)
def RoeFDS( domain, mesh, boundary, parameters, state, gas ):

    print('Roe Scheme: ' + 'CFL = ' + str(parameters.CFL))
    print('________________________________________________________________________________________________________________________________________')
    print('                          mass          u            v        energy')
    print('________________________________________________________________________________________________________________________________________')

    n = 0

    # initialize phi and p state vectors
    Phi = np.zeros( (domain.M+2, domain.N+2, 4) )
    PhiE = np.zeros( (domain.M+2, domain.N+2, 4) )
    Psi = np.zeros( (domain.M+2, domain.N+2, 4) )
    #Phi[:,:,0] = np.ones( (domain.M+2, domain.N+2) )

    P_zeta = np.zeros( (domain.M+1, domain.N+2, 4) )
    P_zeta[:,:,0] = np.zeros( (domain.M+1, domain.N+2) )
    P_zeta[:,:,3] = np.zeros( (domain.M+1, domain.N+2) )

    P_eta = np.zeros( (domain.M+2, domain.N+1, 4) )
    P_eta[:,:,0] = np.zeros( (domain.M+2, domain.N+1) )
    P_eta[:,:,3] = np.zeros( (domain.M+2, domain.N+1) )

    # initialize Psi vector components
    Psi_zeta = np.zeros( (domain.M+1, domain.N+2, 4) )
    Psi_zeta[:,:,1] = mesh.s_proj[1:,:,0]/mesh.s_proj[1:,:,4]
    Psi_zeta[:,:,2] = mesh.s_proj[1:,:,1]/mesh.s_proj[1:,:,4]

    Psi_eta = np.zeros( (domain.M+2, domain.N+1, 4) )
    Psi_eta[:,:,1] = mesh.s_proj[:,1:,2]/mesh.s_proj[:,1:,5]
    Psi_eta[:,:,2] = mesh.s_proj[:,1:,3]/mesh.s_proj[:,1:,5]

    # normal vectors
    N_zeta = np.zeros( (domain.M+1, domain.N+2, 4) )
    N_zeta[:,:,1] = mesh.s_proj[0:-1,:,0]/mesh.s_proj[0:-1,:,4]
    N_zeta[:,:,2] = mesh.s_proj[0:-1,:,1]/mesh.s_proj[0:-1,:,4]

    N_eta = np.zeros( (domain.M+2, domain.N+1, 4) )
    N_eta[:,:,1] = mesh.s_proj[:,0:-1,2]/mesh.s_proj[:,0:-1,5]
    N_eta[:,:,2] = mesh.s_proj[:,0:-1,3]/mesh.s_proj[:,0:-1,5]

    E_hat_left = np.zeros( (domain.M, domain.N, 4), dtype='float', order='F' )
    E_hat_right = np.zeros( (domain.M, domain.N, 4), dtype='float', order='F' )
    F_hat_bot = np.zeros( (domain.M, domain.N, 4), dtype='float', order='F' )
    F_hat_top = np.zeros( (domain.M, domain.N, 4), dtype='float', order='F' )

    Ec_half = np.zeros( (domain.M+1, domain.N+2, 4), dtype='float', order='F' )
    Fc_half = np.zeros( (domain.M+2, domain.N+1, 4), dtype='float', order='F' )

    Ed_half = np.zeros( (domain.M+1, domain.N+2, 4), dtype='float', order='F' )
    Fd_half = np.zeros( (domain.M+2, domain.N+1, 4), dtype='float', order='F' )

    state.residual = np.zeros( [domain.M, domain.N, 4], dtype='float', order='F' )
    state.res = np.ones( [parameters.iterations + 1, 4] )

    mesh.dV4 = np.dstack([mesh.dV[1:-1,1:-1], mesh.dV[1:-1,1:-1], mesh.dV[1:-1,1:-1], mesh.dV[1:-1,1:-1]])

    t = TicToc()

    while n <= parameters.iterations and max(state.res[n-1+np.int(n<10),:]) > parameters.tolerance: 

        t.tic()

        n = n+1

        # state at previous timestep, use for outflow BCs
        state.Qn = state.Q

        # local timestepping
        state = local_timestep( domain, mesh, state, parameters, gas )

        # simplify variable notation from state vector
        state.u = state.Q[:,:,1] / state.Q[:,:,0]
        state.v = state.Q[:,:,2] / state.Q[:,:,0]
        state.ht = thermo.calc_rho_et(state.p, state.Q[:,:,0], state.u, state.v, gas.gamma_fn(gas.Cp, gas.Cv)) / \
                                      state.Q[:,:,0] + state.p/state.Q[:,:,0]

        # initialize Phi vector components
        Phi[:,:,0] = state.Q[:,:,0]
        Phi[:,:,1] = state.Q[:,:,0]*state.u
        Phi[:,:,2] = state.Q[:,:,0]*state.v
        Phi[:,:,3] = state.Q[:,:,0]*state.ht

        PhiE[:,:,0] = state.Q[:,:,0]*state.Q[:,:,0]
        PhiE[:,:,1] = state.Q[:,:,0]*state.u
        PhiE[:,:,2] = state.Q[:,:,0]*state.v
        PhiE[:,:,3] = thermo.calc_rho_et(state.p, state.Q[:,:,0], state.u, state.v, gas.gamma_fn(gas.Cp, gas.Cv))

        Psi_zeta[:,:,3] = state.U[1:,:]
        Psi_eta[:,:,3]  = state.V[:,1:]

        # calculate central term in eqch computational direction
        Ec_half =  (1/2) * ( F_bar( Phi[0:-1,:,:], state.U[0:-1,:], N_zeta, state.p[0:-1,:], domain.M+1, domain.N+2 ) + \
                             F_bar( Phi[1:,:,:], state.U[1:,:], N_zeta, state.p[1:,:], domain.M+1, domain.N+2 ) )
        Fc_half =  (1/2) * ( F_bar( Phi[:,0:-1,:], state.V[:,0:-1], N_eta, state.p[:,0:-1], domain.M+2, domain.N+1 ) + \
                             F_bar( Phi[:,1:,:], state.V[:,1:], N_eta, state.p[:,1:], domain.M+2, domain.N+1 ) )

        # upwind dissipation
        D_zeta = state.eig[0,0,:,:]
        D_eta  = state.eig[1,0,:,:]

        # equations 13-16 in Ren et Al 2011.
        Pu_zeta = np.maximum( 0, state.c[1:,:] - np.abs(state.U[1:,:]) ) * state.Q[1:,:,0]*( state.U[1:,:]-state.U[0:-1,:] )
        Pp_zeta = np.sign(state.U[1:,:]) * np.minimum( np.abs(state.U[1:,:]), state.c[1:,:] ) * ( state.p[1:,:]-state.p[0:-1,:] )/state.c[1:,:]
        Uu_zeta = np.sign(state.U[1:,:]) * np.minimum( np.abs(state.U[1:,:]), state.c[1:,:] ) * ( state.U[1:,:]-state.U[0:-1,:] )/state.c[1:,:]
        Up_zeta = np.maximum( 0, state.c[1:,:]-np.abs(state.U[1:,:])) * ( state.p[1:,:]-state.p[0:-1,:] ) / (state.Q[1:,:,0]*state.c[1:,:]**2)

        Pu_eta  = np.maximum( 0, state.c[:,1:] - np.abs(state.V[:,1:]) ) * state.Q[:,1:,0]*( state.V[:,1:]-state.V[:,0:-1] )
        Pp_eta  = np.sign(state.V[:,1:]) * np.minimum( np.abs(state.V[:,1:]), state.c[:,1:] ) * ( state.p[:,1:]-state.p[:,0:-1] )/state.c[:,1:]
        Uu_eta  = np.sign(state.V[:,1:]) * np.minimum( np.abs(state.V[:,1:]), state.c[:,1:] ) * ( state.V[:,1:]-state.V[:,0:-1] )/state.c[:,1:]
        Up_eta  = np.maximum( 0, state.c[:,1:]-np.abs(state.V[:,1:]) ) * ( state.p[:,1:]-state.p[:,0:-1] ) / (state.Q[:,1:,0]*state.c[:,1:]**2)

        # numerical dissipation terms
        for i in range(0, 4):
            Ed_half[:,:,i] = -(1/2) * ( D_zeta[1:,:] * (PhiE[1:,:,i]-PhiE[0:-1,:,i]) + (Pu_zeta+Pp_zeta)*Psi_zeta[:,:,i] + \
                                                                                       (Uu_zeta+Up_zeta)*Phi[1:,:,i] )
            Fd_half[:,:,i] = -(1/2) * ( D_eta[:,1:] * (PhiE[:,1:,i]-PhiE[:,0:-1,i]) +  (Pu_eta+Pp_eta)*Psi_eta[:,:,i] + \
                                                                                       (Uu_eta+Up_eta)*Phi[:,1:,i] )

        # flux summation
        E_hat_left  = Ec_half[0:-1,1:-1,:] + Ed_half[0:-1,1:-1,:]
        E_hat_right = Ec_half[1:,1:-1,:] + Ed_half[1:,1:-1,:]
        F_hat_bot   = Fc_half[1:-1,0:-1,:] + Fd_half[1:-1,0:-1,:]
        F_hat_top   = Fc_half[1:-1,1:,:] + Fd_half[1:-1,1:,:]


        # flux vector reconstruction
        # flux.face_flux( mdot_half_zeta, mdot_half_eta, Phi, P_zeta, P_eta, E_hat_left, E_hat_right, F_hat_bot, F_hat_top, domain.M, domain.N)

        # update residuals and state vector at each interior cell, from Fortran 90 subroutine
        flux.residual( state.residual, state.dt[1:-1, 1:-1], E_hat_left, E_hat_right, F_hat_bot, F_hat_top,\
                          mesh.s_proj[1:-1,1:-1,:], domain.M, domain.N ) 
        state.Q[1:-1,1:-1,:] = state.Qn[1:-1,1:-1,:] + state.residual / mesh.dV4

        # L_inf-norm residual
        state.res[n-1,0] = np.log10( np.max(state.residual[:,:,0] * mesh.dV[1:-1,1:-1]) ) 
        state.res[n-1,1] = np.log10( np.max(state.residual[:,:,1] * mesh.dV[1:-1,1:-1]) ) 
        state.res[n-1,2] = np.log10( np.max(state.residual[:,:,2] * mesh.dV[1:-1,1:-1]) )
        state.res[n-1,3] = np.log10( np.max(state.residual[:,:,3] * mesh.dV[1:-1,1:-1]) ) 

        #state.res[n-1] = np.log10( np.max(state.residual * mesh.dV4) ) 

        # update cell temperatures and pressures
        state.p = thermo.calc_p( state.Q[:,:,0], state.Q[:,:,3], state.u, state.v, gas.gamma_fn(gas.Cp, gas.Cv) )
        state.T = state.p / (gas.R_fn(gas.Cp, gas.Cv) * state.Q[:,:,0])

        # update covariant velocities
        soln_vars.calc_covariant(mesh.s_proj, state.u, state.v, state.U, state.V, domain.M+2, domain.N+2)

        # enforce boundary conditions
        state = enforce_bc(domain, mesh, boundary, parameters, state, gas)

        # print iteration output
        if n % 10 == 0:
            print('Iteration: ' + str(n) + '    ' + str(round(state.res[n-1,0],3)) + '    ' + str(round(state.res[n-1,1],3)) + \
                                           '    ' + str(round(state.res[n-1,2],3)) + '    ' + str(round(state.res[n-1,3],3)) )
            t.toc('Iteration time:')

    print('________________________________________________________________________________________________________________________________________')

    # post processing variables
    state = calc_postvars(state, gas, n)

    return state


def F_bar( Phi, U, normal, p, M, N ):
    Fbar = np.zeros( (M, N, 4) )
    for i in range(0, 4):
        Fbar[:,:,i] = U * Phi[:,:,i] + normal[:,:,i] * p

    return Fbar


def calc_postvars(state, gas, n):

    state.Mach = np.sqrt( (state.Q[:,:,1]/state.Q[:,:,0])**2 + (state.Q[:,:,2]/state.Q[:,:,0])**2 ) / \
                           thermo.calc_c( state.p, state.Q[:,:,0], gas.gamma_fn(gas.Cp, gas.Cv) )
    state.vel = np.sqrt( (state.Q[:,:,1]/state.Q[:,:,0])**2 + (state.Q[:,:,2]/state.Q[:,:,0])**2 )
    state.p0 = (1+((gas.gamma_fn(gas.Cp, gas.Cv)-1)/2)*state.Mach**2)** \
                   (gas.gamma_fn(gas.Cp, gas.Cv)/(gas.gamma_fn(gas.Cp, gas.Cv)-1)) * state.p
    state.T0 = (1+((gas.gamma_fn(gas.Cp, gas.Cv)-1)/2)*state.Mach**2) * state.T
    state.n = n

    return state