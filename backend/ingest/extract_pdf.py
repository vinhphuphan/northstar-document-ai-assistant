
from pathlib import Path

import pymupdf


pdf_path = Path(
    "../data/FPT/2025/BCTC/"
    "FPT_Baocaotaichinh_2025_Kiemtoan_Hopnhat.pdf"
)

output_path = pdf_path.with_suffix(".txt")


def extract_page_text(page: pymupdf.Page) -> tuple[str, str]:
    # Bước 1: Ưu tiên lấy text có sẵn
    text = page.get_text("text", sort=True).strip() # type: ignore

    if text:
        return text, "native"

    # Bước 2: Nếu không có text, chạy OCR
    ocr_page = page.get_textpage_ocr(
        language="vie+eng",
        dpi=300,
        full=True,
    )

    text = page.get_text(
        "text",
        textpage=ocr_page,
        sort=True,
    ).strip() # type: ignore

    return text, "ocr"


def main() -> None:
    with pymupdf.open(pdf_path) as document:
        print(f"PDF pages: {len(document)}")

        with output_path.open("w", encoding="utf-8") as output:
            for page_number, page in enumerate(document, start=1): # type: ignore
                text, method = extract_page_text(page)

                print(
                    f"Page {page_number:02} | "
                    f"rotation={page.rotation:3} | "
                    f"{method:6} | "
                    f"{len(text)} chars"
                )

                output.write(
                    f"\n\n{'=' * 20} "
                    f"PAGE {page_number} | {method} "
                    f"{'=' * 20}\n"
                )
                output.write(text)

        print(f"\nSaved to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
