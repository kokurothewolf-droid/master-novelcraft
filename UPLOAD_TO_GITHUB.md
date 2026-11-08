# Upload to GitHub

1. Extract `master-novelcraft-github.zip` on your computer.
2. Create a GitHub repository named `master-novelcraft`. Choose Public if you want it publicly accessible. Leave the automatic README and license options unchecked because both files are included.
3. On the empty repository page, choose **uploading an existing file**. For a repository that already has files, use **Add file → Upload files**.
4. Open the extracted `master-novelcraft` folder. Select its contents, including the subfolders, and drag them into the upload area. Upload the extracted contents, not the ZIP itself. `README.md`, `LICENSE`, and `SKILL.md` should appear at the repository root.
5. Commit the uploaded files.

The included sources retain separate attribution and terms in `THIRD_PARTY_NOTICES.md`. Review that file before making the repository public.

Optional local package check, run from the extracted folder:

```bash
python3 tests/check_package.py
```

The check uses only Python's standard library. It verifies structure, referenced paths, source-folder count, and manifest integrity; it does not evaluate writing quality.
