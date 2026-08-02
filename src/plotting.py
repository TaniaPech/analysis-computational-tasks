import numpy as np
import matplotlib.pyplot as plt

from config import FIGURES_PATH, TMIN, TMAX, FREQS, CHANNELS

def save_figure(Ccoh, Ccohm, Ccohf, pvals):
    
    times = np.linspace(
        TMIN,
        TMAX,
        Ccoh.shape[3]
    )

    freqs = FREQS

    pairs = []

    for i in range(len(CHANNELS)):
        for j in range(i+1,len(CHANNELS)):
            pairs.append((i,j))


    for i, j in pairs:

        fig, axes = plt.subplots(
            1,
            3,
            figsize=(18,5),
            constrained_layout=True
        )

        im0 = axes[0].imshow(
            Ccoh[j,i,:,:],
            cmap="bwr",
            origin="lower",
            extent=[TMIN, TMAX, 4, 30],
            aspect=((3/Ccoh.shape[3])/(26/Ccoh.shape[2]))
        )

        axes[0].set_title(
            f"{CHANNELS[i]} → {CHANNELS[j]} (Average)"
        )

        axes[0].set_xlabel("Time (s)")
        axes[0].set_ylabel("Frequency (Hz)")

        fy, fx = np.where(pvals[j,i,:,:] < 0.01)

        axes[0].scatter(
            times[fx],
            freqs[fy],
            color="cyan",
            s=5
        )

        im1 = axes[1].imshow(
            Ccohm[j,i,:,:],
            cmap="bwr",
            origin="lower",
            extent=[TMIN, TMAX, 4, 30],
            aspect=((3/Ccohm.shape[3])/(26/Ccohm.shape[2]))
        )

        axes[1].set_title(
            f"{CHANNELS[i]} → {CHANNELS[j]} (Male)"
        )

        axes[1].set_xlabel("Time (s)")

        im2 = axes[2].imshow(
            Ccohf[j,i,:,:],
            cmap="bwr",
            origin="lower",
            extent=[TMIN, TMAX, 4, 30],
            aspect=((3/Ccohf.shape[3])/(26/Ccohf.shape[2]))
        )

        axes[2].set_title(
            f"{CHANNELS[i]} → {CHANNELS[j]} (Female)"
        )

        axes[2].set_xlabel("Time (s)")

        im0.set_clim(-0.2,0.2)
        im1.set_clim(-0.2,0.2)
        im2.set_clim(-0.2,0.2)

        fig.colorbar(
            im2,
            ax=axes,
            label="Imaginary Coherence (Fisher Z)"
        )

        plt.savefig(
            FIGURES_PATH/f"{CHANNELS[i]}_{CHANNELS[j]}.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close(fig)
