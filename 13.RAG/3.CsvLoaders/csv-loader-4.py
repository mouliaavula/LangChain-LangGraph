'''
Objective: Change the source metadata using a CSV column and read a file using a semicolon delimiter.
'''
from pathlib import Path

from langchain_community.document_loaders import CSVLoader


# ========================================
# CREATE SEMICOLON-SEPARATED FILE
# ========================================

file_path = (
    Path(__file__).resolve().parent
    / "special_students_4.csv"
)
# here csv file is semicolon separated not comma separated
file_path.write_text(
    "student_id;name;course;fee\n"
    "S101;Mouli;Python;5000\n"
    "S102;Manish;Java;6000\n",
    encoding="utf-8"
)


# ========================================
# CREATE CSV LOADER
# ========================================

loader = CSVLoader(
    file_path=str(file_path),
    encoding="utf-8",

    source_column="student_id",

    metadata_columns=[
        "course"
    ],

    csv_args={
        "delimiter": ";"
    }
)


# ========================================
# LOAD DOCUMENTS
# ========================================

documents = loader.load()


# ========================================
# DISPLAY RESULTS
# ========================================

print("TOTAL DOCUMENTS:", len(documents))


for number, document in enumerate(
    documents,
    start=1
):

    print("\nDOCUMENT", number)
    print("----------------")

    print("PAGE CONTENT")
    print(document.page_content)

    print("\nSOURCE:")
    print(
        document.metadata["source"]
    )

    print("COURSE:")
    print(
        document.metadata["course"]
    )
    
'''
Instead of the normal comma separator.We supplied:
csv_args={"delimiter": ";"}
Therefore, CSVLoader interprets the fields correctly.

Observation 2 — source_column
We supplied:source_column="student_id"
Therefore, the source metadata becomes:
S101
for Mouli.
And:
S102
for Manish.

Observation 3 — metadata_columns
We selected:course
as metadata. Therefore, the course value appears in metadata.
Because content_columns was not supplied, CSVLoader automatically includes the other non-metadata fields in page_content.

'''
    
