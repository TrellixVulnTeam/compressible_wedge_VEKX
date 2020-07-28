import numpy as np


def MUSCL( Q, eps, kap, limiter ):

    M, N, R = Q.shape

    Qm2_zeta = np.vstack( ( Q[[0],:,:], Q[0:M-2,:,:] ) )
    Qm1_zeta = np.vstack( ( Q[[0],:,:], Q[1:M-1,:,:] ) )
    Qi_zeta =  Q[1:M,:,:]
    Qp1_zeta = np.vstack( ( Q[2:M,:,:], Q[[M-1],:,:] ) )

    QL_half = QL( Qm2_zeta, Qm1_zeta, Qi_zeta, kap, eps, limiter )
    QR_half = QR( Qm1_zeta, Qi_zeta, Qp1_zeta, kap, eps, limiter )

    Qm2_eta = np.hstack( ( Q[:,[0],:], Q[:,0:N-2,:] ) )
    Qm1_eta = np.hstack( ( Q[:,[0],:], Q[:,1:N-1,:] ) )
    Qi_eta =  Q[:,1:N,:]
    Qp1_eta = np.hstack( ( Q[:,2:N,:], Q[:,[N-1],:] ) )

    QB_half = QL( Qm2_eta, Qm1_eta, Qi_eta, kap, eps, limiter )
    QU_half = QR( Qm1_eta, Qi_eta, Qp1_eta, kap, eps, limiter )

    return QL_half, QR_half, QB_half, QU_half


# left or bottom face
def QL( Qm2, Qm1, Qi, kap, eps, limiter ):
    qL = Qm1 + (eps/4) * ( (1-kap)*(Qm1-Qm2)*limiter(rL(Qm2, Qm1, Qi), 1.5) + \
                        (1+kap)*(Qi-Qm1)*limiter(1/(rL(Qm2, Qm1, Qi)+1e-60), 1.5) )
    return qL

def QR( Qm1, Qi, Qp1, kap, eps, limiter ):
    qR = Qi - (eps/4) * ( (1+kap)*(Qi-Qm1)*limiter(1/(rR(Qm1, Qi, Qp1)+1e-60), 1.5) + \
                        (1-kap)*(Qp1-Qi)*limiter(rR(Qm1, Qi, Qp1), 1.5 ) )
    return qR

def rL( Qm2, Qm1, Qi ):
    r = (Qi-Qm1) / (Qm1-Qm2)
    r[np.isnan(r)] = 0
    r[np.isinf(r)] = 0
    return r

def rR( Qm1, Qi, Qp1 ):
    r = (Qi-Qm1) / (Qp1-Qi)
    r[np.isnan(r)] = 0
    r[np.isinf(r)] = 0
    return r


# flux limiter function class
class limiters:
    hquick = lambda r, b: np.maximum( 0, (2*(r+np.abs(r)) / (r+3)) )
    minmod = lambda r, b: np.maximum( 0, np.minimum(1, r) )
    osher = lambda r, b: np.maximum( 0, np.minimum(b, r) )
    ospre = lambda r, b: np.maximum( 0, 1.5*(r**2+r) / (r**2+r+1) )
    vanalbada1 = lambda r, b: np.maximum( 0, ( r**2 + r ) / ( r**2 + 1 ) )
    vanalbada2 = lambda r, b: np.maximum( 0, (2*r) / (r**2 + 1) )
    vanleer = lambda r, b: np.maximum( ( r + np.abs(r) ) / ( 1 + np.abs(r) ), 0 )
    #dowd = lambda r, b: np.maximum( ( r + np.abs(r) ) / ( r**2 + 1 ), 0 )