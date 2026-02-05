import pandas as pd
from pathlib import Path


def write_calls_to_excel(rows: list[dict], filename: str = "servicetitan_kpis.xlsx") -> None:
    """Write aggregated call data to an Excel file.

    Args:
        rows: List of dictionaries with aggregated call data.
        filename: Name of the Excel file to write.
    """
    if not rows:
        # Nothing to write
        df = pd.DataFrame(columns=["date", "hour", "csr_name", "inbound_calls", "answered_calls", "booked_calls"])
    else:
        df = pd.DataFrame(rows)
        # ensure correct column order
        df = df[["date", "hour", "csr_name", "inbound_calls", "answered_calls", "booked_calls"]]

    file_path = Path(filename)
    # Write to Excel, overwriting existing file
    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Calls", index=False)
