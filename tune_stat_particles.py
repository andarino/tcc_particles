# -*- coding: utf-8 -*-

import os
import yatuner
import logging

cc = 'gcc-10'
src = './tcc_particles/downloading_wall_restitution_GPU.c'
parametros_exec = '0.0001 8 10 0.09'
out = './build/sizeTune/downloading_wall_restitution_GPU'
base = '-O3'
metric = 'duration_time'

if not os.path.isdir('./build/timePerf/'):
    try:
        os.makedirs('./build/timePerf/')
    except OSError as error:
        print(error)

optimizers = set(yatuner.utils.fetch_gcc_optimizers(cc=cc)).difference(
    yatuner.utils.fetch_gcc_enabled_optimizers(options=base))
#optimizers.remove('-fipa-pta')

parameters = yatuner.utils.fetch_gcc_parameters(cc=cc)


def comp(optimizers, parameters, additional):
    options = '-std=c11 -lgsl -lgslcblas -lm -pg '
    if additional is not None:
        options += f'{additional} '
        #options += f'-std=c11 -lgsl -lgsflcblas -lm -pg '
    else:
        options += f'{base} '
        #options += f'-std=c11 -lgsl -lgslcblas -lm -pg '

    if optimizers is not None:
        for optimizer in optimizers:
            options += f'{optimizer} '

    if parameters is not None:
        for parameter, val in parameters.items():
            options += f'--param={parameter}={val} '

    res = yatuner.utils.execute(
        f'{cc} {src} {options} -o {out}')
    
    if res['returncode'] != 0:
        raise RuntimeError(res['stderr'])


def run():
    return yatuner.utils.fetch_perf_stat(out)[metric] / 1000


def perf():
    return yatuner.utils.fetch_perf_stat(out)


tuner = yatuner.Tuner(comp,
                    run,
                    optimizers,
                    parameters,
                    call_perf=perf,
                    norm_range=0.99)

# Tuning process
tuner.initialize()
tuner.test_run(num_samples=200, warmup=10)
tuner.hypotest_optimizers(num_samples=5, num_epochs=30)
tuner.hypotest_parameters(num_samples=5)
# tuner.optimize(num_samples=10, num_epochs=50) #Using bayesian optimization 
tuner.optimize_linUCB(alpha=0.25,
                      num_bins=30,
                      num_epochs=200,
                      nth_choice=4,
                      metric=metric) #using linUCB
tuner.run(num_samples=50)
tuner.plot_data()
