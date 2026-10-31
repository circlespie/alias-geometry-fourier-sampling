# Author publication steps

Everything in this directory is prepared locally. No remote has been created,
no push has been performed, and no release or DOI has been published.

1. Review `CLAIMS.md` and `CLAIMS_REPORT.md`; run `make all` and `make test`.
   Create an empty public GitHub repository named
   `alias-geometry-fourier-sampling` under the author's chosen account. Do not
   initialize it with a separate README or license. From this directory run:

   ```sh
   git remote add origin https://github.com/OWNER/alias-geometry-fourier-sampling.git
   git push -u origin main
   git tag -a v1.0 -m "v1.0 verification companion"
   git push origin v1.0
   ```

   Replace `OWNER` with the intended account before running these commands.

2. Sign into Zenodo using the author's account. Connect GitHub and enable this
   repository in Zenodo's GitHub integration **before publishing the GitHub
   release**. Publish the GitHub release for tag `v1.0`. Verify that Zenodo
   ingests it, check its metadata and license, and record both the release DOI
   and concept DOI. Use the version-specific release DOI for an immutable paper
   snapshot. If automatic integration is unavailable, deposit the tagged source
   archive manually and publish that Zenodo record.

3. Replace `REPO_URL` and `DOI_URL` in the paper's reproducibility line and
   this README. Activate `repository-code` and `doi` in `CITATION.cff` with
   valid values (the DOI field takes a bare DOI). Rebuild the paper through its
   established LaTeX procedure and verify the links. Commit the metadata changes
   and push them. Do not move the `v1.0` tag or imply its archived files contain
   a DOI assigned after release; use a subsequent patch release if an archived
   snapshot containing the final metadata is desired.

4. Submit the LaTeX source to arXiv with the filled-in reproducibility line.
   Optionally include the `v1.0` repository snapshot as ancillary files. Once
   assigned, replace `ARXIV_URL` and the `ARXIV_ID` comment with the actual
   paper identifier. Keep the paper DOI distinct from the software archive DOI.
