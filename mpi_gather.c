#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <assert.h>

float *create_nums(int rank) {
    float *rand_nums = (float *)malloc(sizeof(float) * 5);
    assert(rand_nums != NULL);
    int i;
    for (i = 0; i < 5; i++) {
        rand_nums[i] = (rank + 1) * i;
    }
    return rand_nums;
}

int main() {
    MPI_Init(NULL, NULL);

    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    int size;
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    float *nums = NULL;
    for(int i = 0; i < 2; i++) {
        MPI_Barrier(MPI_COMM_WORLD);

        nums = create_nums(rank);

        float *total_nums = NULL;
        if(rank == 0) {
            total_nums = (float *)malloc(sizeof(float) * 5 * size);
            assert(total_nums != NULL);
        }

        MPI_Gather(nums, 5, MPI_FLOAT, total_nums, 5, MPI_FLOAT, 0, MPI_COMM_WORLD);

        if (rank == 0) {
            for(int i = 0; i < 5*size; i++) {
                if(i % 5 == 0) printf("\n");
                printf("%f ", total_nums[i]);
            }
            printf("\n");
        }

        if (rank == 0) {
            free(total_nums);
        }
        free(nums);
    }

    MPI_Barrier(MPI_COMM_WORLD);
    MPI_Finalize();
}