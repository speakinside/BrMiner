import joblib
import numpy as np
import tqdm


def rbf(x, center, sigma):
    # norm = 1 / (np.sqrt(2*np.pi)*sigma)
    return np.exp(-np.square((x - center)) / (2 * sigma**2))


class TqdmParallel(joblib.Parallel):

    def __call__(self, iterable):
        from collections.abc import Sized

        self._total = None
        if isinstance(iterable, Sized):
            self._total = len(iterable)

        with tqdm.tqdm(total=self._total) as self._progbar:
            return super().__call__(iterable)

    def print_progress(self):
        if self._total is None:
            self._progbar.total = self.n_dispatched_tasks
        self._progbar.n = self.n_completed_tasks
        self._progbar.refresh()
