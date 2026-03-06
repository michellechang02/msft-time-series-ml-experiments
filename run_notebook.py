
#!/usr/bin/env python3
import argparse
from pathlib import Path
import datetime as dt
import papermill as pm


def main():
    script_dir = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(
        description="Run the time-series ensemble notebook using Microsoft.csv from the repo root by default."
    )
    parser.add_argument(
        "--csv",
        default=str(script_dir / "Microsoft.csv"),
        help="Path to the input CSV. Defaults to Microsoft.csv next to run_notebook.py."
    )
    parser.add_argument(
        "--notebook",
        default=str(script_dir / "time_series_ml_ensemble_learning.ipynb"),
        help="Path to the input notebook template."
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Path to the executed output notebook. Defaults to outputs/<notebook_stem>__<timestamp>.ipynb"
    )
    args = parser.parse_args()

    csv_path = Path(args.csv).resolve()
    nb_in = Path(args.notebook).resolve()

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")
    if not nb_in.exists():
        raise FileNotFoundError(f"Notebook not found: {nb_in}")

    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = script_dir / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.out:
        nb_out = Path(args.out)
    else:
        nb_out = out_dir / f"{nb_in.stem}__{ts}.ipynb"

    pm.execute_notebook(
        input_path=str(nb_in),
        output_path=str(nb_out),
        parameters={"CSV_PATH": str(csv_path)},
        cwd=str(script_dir),
        log_output=True,
    )

    print(f"✅ Executed notebook written to: {nb_out}")


if __name__ == "__main__":
    main()
