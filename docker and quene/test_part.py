import Mainpart
import numpy as np
import tracemalloc
import cProfile
#import linecache
import pstats
tracemalloc.start()
#type[pytest test_part.py]
#now do unit tests
#run [pytest file.py ] to make it run, 
#using pytest, only functions with  [def testcase1()] works, main part does not work
def test_Invalid_Datatype_A():
    input1 = "not a matrix"
    input2 = [ [2,4] ,[ 5, 6],[9,10] ]
    result = Mainpart.multiply_matrices(input1,input2)
    #"result" is only the return value, not include print in function
    assert result == -1

def test_Invalid_Datatype_B():
    input1 = [ [3,3,7] ,[2, 1,8] ]
    input2 = 4
    result = Mainpart.multiply_matrices(input1,input2)
    assert result == -2

def test_row_length_mismatch_A():
    input1 =  [ [3,3,7] ,[2, 1,8,6] ]
    input2 = [ [2,4] ,[ 5,6 ], [9,10] ]
    result = Mainpart.multiply_matrices(input1,input2)
    assert result == -3

def test_row_length_mismatch_B():
    input1 =  [ [3,3,7] ,[2, 1,8] ]
    input2 = [ [2,4] ,[ 5 ], [9,10] ]
    result = Mainpart.multiply_matrices(input1,input2)
    assert result == -4

def test_emptyA():
    input1 =  []
    input2 = [ [2,4] ,[ 5,6 ], [9,10] ]
    result = Mainpart.multiply_matrices(input1,input2)
    assert result == -5

def test_emptyB():
    input1 =  [ [3,3,7] ,[2, 1,8] ]
    input2 = []
    result = Mainpart.multiply_matrices(input1,input2)
    assert result == -6

def test_ColumnA_is_not_RowB():
    input1 = [ [3,3,7] ,[ 2, 1,8] ]
    input2 = [ [2,4] ,[ 5, 6],[9,10],[11,12] ]
    result = Mainpart.multiply_matrices(input1,input2)
    assert result == -7

def test_true_case():
    input1 = [ [3,3,7] ,[ 2, 1,8] ]
    input2 = [ [2,4] ,[ 5, 6],[9,10] ]
    result = Mainpart.multiply_matrices(input1,input2)
    compare =[ [84 ,100],[ 81,  94] ]
    assert np.allclose(result, compare)

def main():
    test_Invalid_Datatype_A()
    test_Invalid_Datatype_B()
    test_row_length_mismatch_A()
    test_row_length_mismatch_B()
    test_emptyA()
    test_emptyB()
    test_ColumnA_is_not_RowB()
    test_true_case()

if __name__ == '__main__':

 #now start CPU display with help of import cProfile and pstats

    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    #stats = pstats.Stats(profiler).sort_stats()
    # stats = pstats.Stats(profiler).sort_stats('cumtime')
    print("\n\n cProfile test:")
    stats.print_stats()



 #now start memory part in lineno and traceback method accordingly
    snapshot = tracemalloc.take_snapshot() #take record of current memeory situation

    top_stats_lineno = snapshot.statistics('lineno') #transfer current memeory situation into lineno state
    print("\n\n tracemalloc lineno test:")
    print("[ Top 15 ] for lineno") #print menory situation now in lineneo state
    for stat in top_stats_lineno[:15]:
       print(stat)


    top_stats_traceback = snapshot.statistics('traceback')#transfer current memeory situation into traceback state
    stat_traceback = top_stats_traceback[0]# pick the biggest memory block
    print("\n\n tracemalloc traceback test:")
    print("%s memory blocks: %.1f KiB" % (stat_traceback.count, stat_traceback.size / 1024))
    for line in stat.traceback.format():
       print(line)