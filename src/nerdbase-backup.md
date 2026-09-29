# nerdbase-backup

**Personal Google Drive access with rclone.**

nerdbase-backup is a private, owner-operated desktop integration. It uses
[rclone](https://rclone.org/) to make the owner's Google Drive available as a
folder in a local file manager. Files are downloaded on demand, cached locally,
and uploaded in the background after the owner saves or copies files into the mounted folder.
A local status display reports background uploads and queued files.

The OAuth client is intended solely for the maintainer's own Google account.
Other users are not supported and should not authorize it.

Despite its name, this is a live mount, not a backup: deletions and overwrites
in the mounted folder are applied to Google Drive.

This is not a public cloud-storage service. There is no account registration,
developer-operated file server, advertising, or analytics in the integration.
It is not affiliated with or endorsed by Google or the rclone project.

## Google access

The integration requests Google Drive access so the owner can list, open,
create, change, move and delete their existing files and folders. The narrower
permission for files created by the app would not provide access to the owner's
existing Drive library. Google authorization takes place in the browser; the
integration does not receive the owner's Google password.

## Privacy and terms

- [Privacy policy](../nerdbase-backup-privacy/)
- Access can be revoked in [Google Account connections](https://myaccount.google.com/connections).
  Complete or preserve pending uploads before revoking access or removing the cache.
- Personal use only; no hosted storage, availability commitment or support SLA
  is provided. Keep independent backups of important files.
- Google Drive remains subject to [Google's terms](https://policies.google.com/terms).
  rclone is distributed under its [MIT license](https://rclone.org/licence/).
- Maintainer: [nerdislb on GitHub](https://github.com/nerdislb).
  General questions can be raised in the
  [site repository](https://github.com/nerdislb/nbsystems.dev/issues).
  For private matters, use the support email shown on the Google consent screen.
  Do not post credentials or private file information in public issues.
