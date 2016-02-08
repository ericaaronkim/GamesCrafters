from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def fun(*args):
	return args/2 == 0

#Scatter
data = comm.scatter(data, root=0)
if fun(data):
	comm.send(True, dest = 0, tag = 1)
else:
	comm.send(False, dest = 0, tag = 0)

#Gather
data = comm.gather(data, root=0)

comm.Barrier()

if rank == 0:
    print data