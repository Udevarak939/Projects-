import argparse
import os
from pathlib import Path
import boto3


def upload_directory(local_dir: str, bucket: str, prefix: str) -> int:
    root = Path(local_dir)
    if not root.exists():
        raise FileNotFoundError(root)
    s3 = boto3.client("s3")
    count = 0
    for path in root.rglob("*"):
        if path.is_file():
            key = f"{prefix.rstrip('/')}/{path.relative_to(root).as_posix()}"
            s3.upload_file(str(path), bucket, key)
            print(f"uploaded s3://{bucket}/{key}")
            count += 1
    return count


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Upload Olist raw files to S3")
    p.add_argument("--local-dir", default="data/raw")
    p.add_argument("--bucket", default=os.getenv("S3_BUCKET"))
    p.add_argument("--prefix", default=os.getenv("S3_RAW_PREFIX", "olist/raw"))
    args = p.parse_args()
    if not args.bucket:
        raise SystemExit("Set --bucket or S3_BUCKET")
    print(f"Uploaded {upload_directory(args.local_dir, args.bucket, args.prefix)} files")
