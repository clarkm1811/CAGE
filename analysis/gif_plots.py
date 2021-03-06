#!/usr/bin/env python3
import imageio
import glob


def main():

    # runs = [64, 44, 66, 48, 70, 50, 72, 54, 60, 42] #starting at 7.5mm so if doesn't show up in ppt at least will show a plot with alphas
    # plot_dir = './plots/normScan/cal_normScan/'

    plot_dir = './plots/angleScan/'
    radii = ['10', '15', '18']

    dsp_params = ['alp_energy_', 'alp_AoE_', 'alp_DCR_', 'alp_AoEvDCR_', 'alp_DCRvTp050_']
    outputs_files = ['energy.gif', 'aoeVsE.gif', 'dcrVsE.gif', 'aoeVsdcr.gif', 'dcrVstp0_50.gif']

    # dsp_gif(dsp_params, runs, plot_dir, outputs_files)
    dsp_gif_byRadius(dsp_params, radii, plot_dir, outputs_files)

def dsp_gif(dsp_params, runs, plot_dir, outputs_files):

    for param, outfile in zip(dsp_params, outputs_files):
        images = []
        for run in runs:
            images.append(imageio.imread(f'{plot_dir}{param}{run}.png'))

        imageio.mimsave(f'{plot_dir}{outfile}', images, fps=3)
        print('Saving ', f'{plot_dir}{outfile}')

def dsp_gif_byRadius(dsp_params, radii, plot_dir, outputs_files):

    for param, outfile in zip(dsp_params, outputs_files):
        for radius in radii:
            images = []
            for file in sorted(glob.glob(f'{plot_dir}normalized_{param}{radius}*.png'), reverse=True):
                print(radius, file)
                images.append(imageio.imread(file))

            imageio.mimsave(f'{plot_dir}normalized_{radius}mm_{outfile}', images, fps=1)
            print('Saving ', f'{plot_dir}normalized_{radius}mm_{outfile}')


if __name__=="__main__":
    main()
