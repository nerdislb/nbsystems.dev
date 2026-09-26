# nbOS Launcher Privacy Policy

Last updated: 2026-09-26

This policy describes nbOS 0.2.0-beta.8 and later (the O1 Home). Older versions that may still be installed are covered
in the section "Earlier versions" below.

nbOS is an Android launcher. It has no accounts, ads, developer-operated analytics or developer-operated data collection.
nbOS does not send your data to the developer.

## Data used by the app

- **Approximate location** is used to request local weather, including a short-term (15-minute) precipitation forecast,
  from [Open-Meteo](https://open-meteo.com/). After you grant location permission, nbOS requests weather automatically
  whenever the Home screen is shown and about every 20 minutes while it stays open (once a minute until a first forecast
  arrives). The provider receives the request coordinates and ordinary network metadata, including your IP address.
  Weather responses are cached on the device.
- **Calendar access** lets nbOS show upcoming events and a countdown on the Home screen. By default nbOS reads all
  calendars that are visible on the device, including calendars added later; in settings you can limit it to selected
  calendars. To offer that choice, nbOS also reads each calendar's name and its account name and type, which can be an
  email address. Calendar data stays on the device and is not sent to the weather service.
- **Installed apps** are listed to provide the app drawer, search and favorites. Battery state is displayed locally.
- **Timer:** when you set a timer on the clock ring, nbOS asks your clock app to start it (Android's set-alarm permission)
  with the duration and the label "nbOS", and stores only the end time on the device to show the remaining time.
- **Widgets** you add are hosted by nbOS. Android passes the widget's ID and size to the app that provides the widget.
- **Files and folders you pick** through Android's system picker are used for wallpapers, theme wallpaper folders and
  manual configuration import/export.
- **Preferences** such as favorites and their order, widget bindings and sizes, wallpaper choices and crops, theme and
  motion settings, permission history and weather preferences are stored locally. Android cloud backup and device
  transfer are disabled for nbOS's app data. When nbOS sets your system wallpaper, the image is handed to Android, which
  may include the system wallpaper in its own backup; that copy is managed by Android, not by nbOS.

Night phosphor, idle drift and all other visual features run entirely on the device.

### Configuration export

Export writes an unencrypted JSON file to the location you choose. It contains your favorites (app package names),
selected calendar IDs, preferences and any retained Todo, Notes and folder content (see below). Timer data, the weather
cache, widget bindings and wallpaper images are not exported. If you save the file to a cloud document provider, that
provider stores it under its own terms.

## Data kept from earlier versions

Removing the Todo, Notes, Habits and folder features did not delete data you saved with them. Previously saved tasks,
notes and folder assignments stay stored on the device and are still included in configuration export for
compatibility; nbOS no longer synchronizes them. Exports can therefore contain personal content — store them securely.
Previously selected sync folders, their external files and granted folder permissions are left unchanged.

## Retention and deletion

App data stays on your device until you change it, clear nbOS's app data, or uninstall nbOS. Exported files, images in
storage you chose and the system wallpaper (including any Android wallpaper backup) remain under your control and are not
removed with nbOS's app data. nbOS has no server-side account or copy of your data to delete.

## Third-party services

Open-Meteo's [terms](https://open-meteo.com/en/terms) state that technical logs can contain IP addresses and coordinates
and are deleted after 90 days; nbOS cannot delete provider logs.

nbOS uses AndroidX EmojiCompat, which can ask the device's system font provider (usually Google Play services) for an
up-to-date emoji font. That request is handled by the provider under its own privacy terms.

Links in settings (privacy policy, licenses and the optional Ko-fi support page) open in your browser. Apps, widgets,
browsers, websites and document providers you use with nbOS have their own privacy practices.

## Earlier versions (0.2.0-beta.7 and older)

Earlier versions additionally offered optional features that are removed in the current version:

- **Todo and Notes sync** through a folder you selected. Before replacing a synced document, nbOS kept app-private
  recovery snapshots of the pending and previous content; they stay on the device until overwritten, until app data is
  cleared or until nbOS is uninstalled.
- **Herdr** requests went only to the snapshot URL you configured. Later releases required HTTPS for it; 0.1.0-beta also
  allowed plain HTTP. Other integrations such as Tailscale or Termux were configured by you and have their own privacy
  practices.
- **Device status** such as memory, storage, network address and uptime was displayed locally.
- **Google ML Kit** was used for the optional experimental depth-clock cutout (subject segmentation; the model could be
  downloaded through Google Play services) and, in versions with desktop approval, for scanning the pairing QR code with
  the camera (barcode scanning). Images and camera frames were processed on the device. The ML Kit SDK can collect
  device and app information, device and per-installation identifiers, performance metrics and feature/error events for
  diagnostics and usage analytics (see Google's [ML Kit Android data
  disclosure](https://developers.google.com/ml-kit/android-data-disclosure)). nbOS cannot delete data already held by
  Google.
- Versions before 0.2.0-beta.6 could optionally be paired with a user-controlled nbshell desktop for **biometric
  approval** of desktop sign-in requests. Pairing sent the phone model, a random device ID and a public signing key to
  the desktop address in the QR code, and a foreground service then checked only that desktop for pending requests.
  Biometric data stayed with Android.

Current versions clean up the retired desktop approval locally on startup (old pairing preferences, key alias and
notification channel); no request is sent to a desktop.

## Contact

- Privacy questions or requests: [privacy@nbsystems.dev](mailto:privacy@nbsystems.dev)
- Product support: [support@nbsystems.dev](mailto:support@nbsystems.dev)
- Security reports (please not in public issues): [security@nbsystems.dev](mailto:security@nbsystems.dev)
