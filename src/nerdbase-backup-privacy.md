# nerdbase-backup Privacy Policy

Last updated: 2026-09-29

This policy covers **nerdbase-backup**, the owner's personal rclone-based desktop
integration with Google Drive. It does not cover nbOS Launcher or other apps.

## Data access and use

The integration accesses Google Drive file contents, names, folder structure,
file metadata and storage-usage information to provide a local mounted folder
and transfer status. Operations requested by the owner can create, change,
move or delete Drive files. Background transfers may continue after the file
manager has finished copying data into the local cache.

OAuth credentials, including refresh tokens, are stored in owner-controlled
local configuration files. The integration does not receive the Google account
password. Downloaded files and pending writes are cached on the owner's device;
local diagnostics can include filenames, transfer details and error messages.

## Sharing

The desktop connects directly to Google to authorize access and transfer data.
There is no developer-operated intermediary receiving Drive files or OAuth
tokens. The integration does not sell Google user data, use it for advertising,
or use it to train AI models. Google API data is used only for this personal
file-access and transfer functionality, in accordance with the
[Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy),
including its Limited Use requirements.

Once files are available in the local folder, the owner may open or process
them with other applications, including AI assistants, sync or backup tools.
Those applications operate separately under their own terms and policies and
may send data to their respective providers. Google processes API requests under its
[privacy policy](https://policies.google.com/privacy).

## Retention, control and deletion

The owner controls the local configuration, cache, logs and any device backups.
Cache policies can evict clean cached files; pending uploads may remain until
successfully transferred. Disconnecting the integration does not automatically
erase local copies, logs, backups or files already stored in Google Drive.

Access can be revoked in
[Google Account third-party connections](https://myaccount.google.com/connections).
After pending transfers have been handled and the mount stopped, the owner can
remove the integration's local credentials and cached data. Remote files and
Drive trash are managed separately in Google Drive. The maintainer and intended
user are the same person; there is no additional integration-operated
server-side account or dataset beyond the owner's devices and Google account.

## This informational website

These static pages contain no analytics scripts, embedded trackers, sign-in
forms or Drive data. They are served by GitHub Pages, whose provider may process
ordinary connection information such as IP addresses under the
[GitHub privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

## Contact

Maintainer: [nerdislb on GitHub](https://github.com/nerdislb). General questions
can be raised in the [site repository](https://github.com/nerdislb/nbsystems.dev/issues).
For private matters, use the support email shown on the Google consent screen.
Do not publish tokens, credentials, filenames or private file contents there.

[Back to nerdbase-backup](../nerdbase-backup/)
