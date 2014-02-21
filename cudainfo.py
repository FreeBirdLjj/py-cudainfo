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
\tPCI Bus ID: %(pci_bus_id)s
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
\tIntegrated: %(integrated)s
\tCan Map Host Memory: %(can_map_host_mem)s
\tMax Texture1D Size in (Width): %(max_texture1d_sz)s
\tMax Texture2D Size in (Width, Height): %(max_texture2d_sz)s
\tMax Texture3D Size in (Width, Height, Depth): %(max_texture3d_sz)s
\tMax Texture2D Array Size in (WIDTH, HEIGHT, NUMSLICES): %(max_texture2d_array_sz)s
\tSurface Alignment: %(surf_align)d
\tConcurrent Kernels: %(concurr_krnl)d
\tEcc Enabled: %(ecc_en)s
\tTCC Driver: %(tcc_drv)s
\tMemory Clock Rate: %(mem_clk_rate)dHz
\tGlobal Memory Bus Width: %(global_mem_bus_width)dbit
\tL2 Cache Size: %(l2_cache_sz)dKB
\tMax Threads Per Multiprocessor: %(max_thrds_per_mp)d
\tAsync Engine Count: %(async_engine_cnt)d
\tUnified Addressing: %(unified_addressing)s
\tMax Texture1D Layered Size in (Width, Layers): %(max_texture1d_layered_sz)s
\tMax Texture2D Gather Size in (Width, Height): %(max_texture2d_gather_sz)s
\tMax Texture3D Size in (Width, Height, Depth) Alternate: %(max_texture3d_alt_sz)s
\tTexture Pitch Alignment: %(texture_pitch_align)d
\tMax TextureCubemap Size in (Width): %(max_texturecubemap_sz)s
\tMax TextureCubemap Layered Size in (Width, Layers): %(max_texturecubemap_layered_sz)s
\tMax Surface1D Size in (Width): %(max_surface1d_sz)s
\tMax Surface2D Size in (Width, Height): %(max_surface2d_sz)s
\tMax Surface3D Size in (Width, Height, Depth): %(max_surface3d_sz)s
\tMax Surface1D Layered Size in (Width, Layers): %(max_surface1d_layered_sz)s
\tMax Surface2D Layered Size in (Width, Height, Layers): %(max_surface2d_layered_sz)s
\tMax SurfaceCubemap Size in (Width): %(max_surfacecubemap_sz)s
\tMax SurfaceCubemap Layered Size in (Width, Layers): %(max_surfacecubemap_layered_sz)s
\tMax Texture1D Linear Size in (Width): %(max_texture1d_linear_sz)s
\tMax Texture2D Linear Size in (Width, Height, Pitch): %(max_texture2d_linear_sz)s
        """ % {
            "cnt": i,
            "name": dev.name(),
            "compute_capability": dev.compute_capability(),
            "pci_bus_id": dev.pci_bus_id(),
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
            "integrated": bool(dev.integrated),
            "can_map_host_mem": bool(dev.can_map_host_memory),
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
            "tcc_drv": bool(dev.tcc_driver),
            "mem_clk_rate": dev.memory_clock_rate,
            "global_mem_bus_width": dev.global_memory_bus_width,
            "l2_cache_sz": dev.l2_cache_size >> 10,
            "max_thrds_per_mp": dev.max_threads_per_multiprocessor,
            "async_engine_cnt": dev.async_engine_count,
            "unified_addressing": bool(dev.unified_addressing),
            "max_texture1d_layered_sz": (dev.maximum_texture1d_layered_width,
                                         dev.maximum_texture1d_layered_layers),
            "max_texture2d_gather_sz": (dev.maximum_texture2d_gather_width,
                                        dev.maximum_texture2d_gather_height),
            "max_texture3d_alt_sz": (dev.maximum_texture3d_width_alternate,
                                     dev.maximum_texture3d_height_alternate,
                                     dev.maximum_texture3d_depth_alternate),
            "texture_pitch_align": dev.texture_pitch_alignment,
            "max_texturecubemap_sz": (dev.maximum_texturecubemap_width),
            "max_texturecubemap_layered_sz": (dev.maximum_texturecubemap_layered_width,
                                              dev.maximum_texturecubemap_layered_layers),
            "max_surface1d_sz": (dev.maximum_surface1d_width),
            "max_surface2d_sz": (dev.maximum_surface2d_width,
                                 dev.maximum_surface2d_height),
            "max_surface3d_sz": (dev.maximum_surface3d_width,
                                 dev.maximum_surface3d_height,
                                 dev.maximum_surface3d_depth),
            "max_surface1d_layered_sz": (dev.maximum_surface1d_layered_width,
                                         dev.maximum_surface1d_layered_layers),
            "max_surface2d_layered_sz": (dev.maximum_surface2d_layered_width,
                                         dev.maximum_surface2d_layered_height,
                                         dev.maximum_surface2d_layered_layers),
            "max_surfacecubemap_sz": (dev.maximum_surfacecubemap_width),
            "max_surfacecubemap_layered_sz": (dev.maximum_surfacecubemap_layered_width,
                                              dev.maximum_surfacecubemap_layered_layers),
            "max_texture1d_linear_sz": (dev.maximum_texture1d_linear_width),
            "max_texture2d_linear_sz": (dev.maximum_texture2d_linear_width,
                                        dev.maximum_texture2d_linear_height,
                                        dev.maximum_texture2d_linear_pitch),
            })
