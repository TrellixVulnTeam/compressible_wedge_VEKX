# wedge grid generation function
def mesh_wedge(domain):

    # import numpy
    import numpy as np
    import python.mesh.grid.meshing as meshing

    # import domain values
    M = domain.M
    N = domain.N
    length = domain.length
    height = domain.height
    theta = domain.theta
    wedge_start = domain.obj_start

    x = np.linspace(-(1/M)*length, length*(1+(1/M)), M+3)
    y = np.linspace(-(1/N)*height, height*(1+(1/N)), N+3)

    xx, yy = np.meshgrid(x, y)
    xx = np.transpose(xx)
    yy = np.transpose(yy)

    meshing.mod2wedge(xx, yy, height, theta, wedge_start, M, N)

    yy = np.fliplr(yy)
    #yy[:,-1] = height*(1+(1/(N)))

    return xx, yy


def mesh_corner(domain):

    # import numpy
    import numpy as np
    import python.mesh.grid.meshing as meshing

    # import domain values
    M = int(domain.M/2)
    N = domain.N
    length = domain.length
    height = domain.height
    theta1 = domain.theta
    af_start = domain.obj_start
    af_end = domain.obj_end

    # mesh left side of domain

    x1 = np.linspace(-(1/M)*length, length*(1+(1/M))/2, M+3)
    y1 = np.linspace(-(1/N)*height, height*(1+(1/N)), N+3)

    xx1, yy1 = np.meshgrid(x1,y1)
    xx1 = np.transpose(xx1)
    yy1 = np.transpose(yy1)

    meshing.mod2wedge(xx1, yy1, height, theta1, af_start, M, N)

    yy1 = np.fliplr(yy1)
    yy1[:,-1] = height*(1+(1/(N)))

    # determine airfoil height
    if np.sign(theta1) == 1:
        h = np.max(yy1[:,1])
    else:
        h = np.min(yy1[:,1])

    # mesh right side of domain

    x2 = np.linspace(0, length/2, M+3) + np.max(xx1)
    y2 = np.linspace(-(1/N)*height, height*(1+(1/N)), N+3)

    xx2, yy2 = np.meshgrid(x2,y2)
    xx2 = np.transpose(xx2)
    yy2 = np.transpose(yy2)

    # determine second half angle
    theta2 = np.arctan(h/((np.max(xx2)-np.min(xx2))-(length-af_end)))

    meshing.mod2wedge(xx2, yy2, height, theta2, (length-af_end)+np.max(xx1), M, N)
    yy2 = np.flipud(yy2)
    yy2 = np.fliplr(yy2)
    yy2[:,-1] = height*(1+(1/(N)))

    xx = np.vstack((xx1[1:-1,:], xx2[0:-1,:]))
    yy = np.vstack((yy1[1:-1,:], yy2[0:-1,:]))

    domain.M = M*2

    return xx, yy


def mesh_cylinder(domain):

    # import numpy
    import numpy as np

    # import domain values
    M = domain.M
    N = domain.N
    length = domain.length
    height = domain.height
    theta1 = domain.theta
    cyl_start = domain.obj_start
    cyl_end = domain.obj_end

    # start = cyl_start*(1-(1/M))
    r = np.linspace( cyl_start*(1-(1/M)), length*(1+(1/M)), M+3 )
    # ratio = r[-1] / (length*(1+(1/M))-start)
    # r = r / ratio
    # r = r + start

    th = np.linspace( -2*np.pi*(3/N/2), 2*np.pi*(1+(3/N/2)), N+3)


    rr, tt = np.meshgrid(r, th)
    xx = rr * np.cos(tt)
    yy = rr * np.sin(tt)

    xx = np.transpose(xx)
    yy = np.transpose(yy)

    return xx, yy


def mesh_naca4(domain):

    import numpy as np
    
    # import domain values
    domain.M = domain.M + int(domain.M%2 == 1)
    M = domain.M
    domain.N = domain.N + int(domain.N%2 == 1)
    N = domain.N
    length = domain.length
    height = domain.height
    thick = domain.theta
    obj_start = domain.obj_start
    obj_end = domain.obj_end

    x = np.linspace(-(1/M)*length, length*(1+(1/M)), M+3)
    y = np.linspace(-height/2*(1+(1/N)), height/2*(1+(1/N)), N+3)

    domain.obj_i = np.where(x>obj_start)
    domain.obj_i = domain.obj_i[0][0]
    domain.obj_f = np.where(x>obj_end)
    domain.obj_f = domain.obj_f[0][0]

    xaf = x[domain.obj_i:domain.obj_f]
    c = np.max(xaf)-np.min(xaf)
    t = thick*c
    yt = NACA4( xaf-np.min(xaf), c, t )

    xx, yy = np.meshgrid(x, y)
    xx = np.transpose(xx)
    yy = np.transpose(yy)

    half = int(N/2)
    domain.wallL = half
    domain.wallU = half+2
    for j in range( 0, half ):
        yy[domain.obj_i:domain.obj_f, int(N/2)-j] = -yt*float((half-j)/half) + yy[domain.obj_i:domain.obj_f, int(N/2)-j]
        yy[domain.obj_i:domain.obj_f, int(N/2+2)+j] = yt*float((half-j)/half) + yy[domain.obj_i:domain.obj_f, int(N/2+2)+j]


    return xx, yy


def NACA4( x, c, t ):
        import numpy as np
        y = 5*t*c * ( 0.2969*np.sqrt(x/c) - 0.126*(x/c) - 0.3516*(x/c)**2 + 0.2843*(x/c)**3 - 0.1015*(x/c)**4 )
        return y