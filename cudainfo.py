#!/usr/bin/env python3

import pycuda.driver
import pycuda.autoinit
import pycuda.compiler
import sys


if __name__ == "__main__":
    prog = sys.argv[0]
    cnt = pycuda.driver.Device.count()

    if cnt == 0:
        print("%s: No devices found!" % prog, file=sys.stderr)
        exit(-1)
    else:
        print("%d device(s) found in total." % cnt)

    for i in range(cnt):
        dev = pycuda.driver.Device(i)
        print("""
Device %(cnt)d:
\tName: %(name)s
\tCompute Capability: %(compute_capability)s
\tTotal Memory: %(total_mem)dMB
\tMax Threads Per Block: %(max_thrds_per_blk)d
\tMax Block Dim in (X, Y, Z): %(max_blk_dim)s
\tMax Grid Dim in (X, Y, Z): %(max_grid_dim)s
\tMax Shared Memory Per Block: %(max_shared_mem_per_blk)dKB
\tTotal Constant Memory: %(total_const_mem)dKB
\tWarp Size: %(warp_sz)d
\tMax Pitch: %(max_pitch)d
\tMax Registers Per Block: %(max_regs_per_blk)d
\tClock Rate: %(clock_rate)dMHz
\tTexture Alignment: %(texture_align)d
\tGPU Overlap: %(gpu_overlap)d
\tMultiprocessor Count: %(mp_cnt)d
\tKernel Execution Timeout: %(krnl_exec_timeout)d
\tIntegrated: %(integrated)d
\tCan Map Host Memory: %(can_map_host_mem)d
\tMax Texture1D Size in (WIDTH): %(max_texture1d_sz)s
\tMax Texture2D Size in (WIDTH, HEIGHT): %(max_texture2d_sz)s
\tMax Texture3D Size in (WIDTH, HEIGHT, DEPTH): %(max_texture3d_sz)s
\tMax Texture2D Array Size in (WIDTH, HEIGHT, NUMSLICES): %(max_texture2d_array_sz)s
\tSurface Alignment: %(surf_align)d
\tConcurrent Kernels: %(concurr_krnl)d
\tEcc Enabled: %(ecc_en)s
\tPCI BUS ID: %(pci_bus_id)s
\t
        """ % {
            "cnt": i,
            "name": dev.name(),
            "compute_capability": dev.compute_capability(),
            "total_mem": dev.total_memory() >> 20,
            "max_thrds_per_blk": dev.max_threads_per_block,
            "max_blk_dim": (dev.max_block_dim_x,
                            dev.max_block_dim_y,
                            dev.max_block_dim_z),
            "max_grid_dim": (dev.max_grid_dim_x,
                             dev.max_grid_dim_y,
                             dev.max_grid_dim_z),
            "max_shared_mem_per_blk": dev.max_shared_memory_per_block >> 10,
            "total_const_mem": dev.total_constant_memory >> 10,
            "warp_sz": dev.warp_size,
            "max_pitch": dev.max_pitch,
            "max_regs_per_blk": dev.max_registers_per_block,
            "clock_rate": dev.clock_rate >> 20,
            "texture_align": dev.texture_alignment,
            "gpu_overlap": dev.gpu_overlap,
            "mp_cnt": dev.multiprocessor_count,
            "krnl_exec_timeout": dev.kernel_exec_timeout,
            "integrated": dev.integrated,
            "can_map_host_mem": dev.can_map_host_memory,
            "max_texture1d_sz": (dev.maximum_texture1d_width),
            "max_texture2d_sz": (dev.maximum_texture2d_width,
                                 dev.maximum_texture2d_height),
            "max_texture3d_sz": (dev.maximum_texture3d_width,
                                 dev.maximum_texture3d_height,
                                 dev.maximum_texture3d_depth),
            "max_texture2d_array_sz": (dev.maximum_texture2d_array_width,
                                       dev.maximum_texture2d_array_height,
                                       dev.maximum_texture2d_array_numslices),
            "surf_align": dev.surface_alignment,
            "concurr_krnl": dev.concurrent_kernels,
            "ecc_en": bool(dev.ecc_enabled),
            "pci_bus_id": dev.pci_bus_id,
            })
