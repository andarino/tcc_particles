# -*- coding: utf-8 -*-

import os
import yatuner

cc = 'gcc-10'
src = './tcc_particles/downloading_wall_restitution_GPU.c'
out = './build/downloading_wall_restitution_GPU'
base = '-Os'

#making build directory if necessary
if not os.path.isdir('./build'):
    os.mkdir('./build')

optimizers = set(yatuner.utils.fetch_gcc_optimizers(cc=cc)).difference(
        yatuner.utils.fetch_gcc_enabled_optimizers(options=base))
optimizers.remove('-fipa-pta')
parameters = yatuner.utils.fetch_gcc_parameters(cc=cc)


def comp(optimizers, parameters, additional):
    options = ''
    if additional is not None:
        #options += f'{additional} ' 
        options += f'-std=c11 -lgsl -lgslcblas -lm -pg {base} '
    else:
        options += f'-std=c11 -lgsl -lgslcblas -lm -pg {base} '

    if optimizers is not None:
        for optimizer in optimizers:
            options += f'{optimizer} '

    if parameters is not None:
        for parameter, val in parameters.items():
            options += f'--param={parameter}={val} '

    res = yatuner.utils.execute(f'{cc} {src} {options} -o {out}')
    #gcc downloading_wall_restitution_GPU.c -o downloading_wall_restitution_GPU -std=c11 -lgsl -lgslcblas -lm -pg -O3
    #./downloading_wall_restitution_GPU 0.0001 8 10 0.09'
    if res['returncode'] != 0:
        raise RuntimeError(res['stderr'])


def run():
    return yatuner.utils.fetch_size(out)


def perf():
    return NotImplementedError()

tuner = yatuner.Tuner(call_compile = comp,
                      call_running =run,
                      optimizers = optimizers,
                      parameters = parameters,
                      call_perf=perf,
                      norm_range=0.99,
                      workspace='yatuner_size.db',
                      deterministic=True)

tuner.initialize()
tuner.test_run(num_samples=1, warmup=0)
tuner.hypotest_optimizers(num_samples=1, num_epochs=30)
tuner.hypotest_parameters(num_samples=1)
tuner.optimize(num_samples=1, num_epochs=50)
tuner.run(num_samples=1)
