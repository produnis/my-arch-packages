# my-arch-packages
manage a list of your favourite arch and aur packages and install them if needed. All information is saved to a local `sqlite3` database file.


## Installation

- Open `my-arch-packages.py` in a text editor and change the path to the database to your setting.
- make it executable (e.g. `chmod +x my-arch-packages.py`)


## Usage

`my-arch-packages.py [-h] [-a ADD] [-d DELETE] [-p] <PACKAGE>`

### Options


| Option  | Description |
|---|---|
| `-h`, `--help`   | show this help message and exit |
| `-a`, `--add ADD` | add package to database    |
| `-d`, `--delete` | delete package from database |
|`-p`, `--print` | print intsall command |


## Examples

adding a new package, e.g. `neofetch`:
- `$ my-arch-packages.py -a neofetch`

deleting a package, e.g. `neofetch`:
- `$ my-arch-packages.py -d neofetch`

print the install command:
- `$ my-arch-packages.py -p`

My personal install command looks like this:

```
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- 
# So, you want to install all your pacakges to a fresh Arch, hm?
# Let's start with non-AUR packages:
# ----------------------------------
pacman -S --needed accountsservice apache arc-icon-theme archlinux-keyring arrow asciiquarium audacious audacity avidemux-cli avidemux-qt bash-completion biber bind-tools bluefish calibre catfish chromaprint chromium cmake code cronie cryfs cups-pdf curl digikam dmidecode easytag egl-wayland element-desktop elementary-icon-theme encfs evince fatsort ffmpeg ffmpegthumbnailer figlet file firefox-i18n-de gcc-fortran gdal geany gedit geeqie geoip gimp git glxinfo gnome-calculator gnome-disk-utility gnome-icon-theme-extras gnome-keyring gnumeric gparted gramps graphviz gtk-theme-elementary gvfs gvfs-smb handbrake-cli haveged hddtemp hexchat hunspell-de id3v2 imagemagick inkscape inxi kde-applications-meta keepassxc kile kmymoney kodi-eventclients krename ksshaskpass kstars kvantum kvantum-theme-materia lame libdvdcss libreoffice-still-de libvdpau links linux-headers lxde-icon-theme lynx mac mariadb mate-icon-theme mencoder mkvtoolnix-cli mkvtoolnix-gui mlocate mpc mplayer ncdu nemo nemo-fileroller neofetch neovim net-tools network-manager-applet nextcloud-client nfs-utils noto-fonts noto-fonts-cjk noto-fonts-emoji ntp nyx obsidian openbsd-netcat opencl-nvidia openssh openvpn osm-gps-map owncloud-client oxygen-icons p7zip pacman-contrib pageedit pandoc papirus-icon-theme pavucontrol pdfgrep pdfmixtool pdftk perl-image-exiftool php picard pkgfile plasma-meta plasma-wayland-session python python-pip python-requests qrencode r reflector remmina rkward rsnapshot rsync screen sddm shotwell sigil signal-desktop smplayer socat sound-theme-elementary soundconverter sshfs sshuttle sudo syncthing telegram-desktop texlive-bibtexextra texlive-core texlive-fontsextra texlive-fontsrecommended texlive-humanities texlive-latexextra texlive-pictures texlive-plaingeneric texlive-xetex thunar-archive-plugin thunar-media-tags-plugin thunar-volman thunderbird-i18n-de tokodon tor torsocks transmission-cli transmission-gtk trash-cli tumbler ufw unison unoconv unzip usbutils veracrypt vim vlc vorbis-tools webp-pixbuf-loader wget whois wine x11-ssh-askpass xarchiver xclip xf86-input-wacom xf86-video-nouveau xfce4-goodies xfce4-screenshooter xorg-font-util xorg-fonts-100dpi xorg-fonts-75dpi xorg-fonts-encodings xorg-fonts-misc xorg-fonts-type1 xorg-mkfontscale yakuake zbar zenity zip 
 
 
# Time to install 'yay' for easy AUR-installations: 
# -------------------------------------------------
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
 
 
# Now you can simply install all these AUR-packages: 
# --------------------------------------------------
yay -S --needed anki-official-binary-bundle briss cryptomator davfs2 dexy-icons-git dexy-theme-git dupeguru epson-inkjet-printer-escpr esniper fslint gnome-search-tool jdownloader2 lumi matrix-commander mcomix mp3val nodejs-decktape parajve portfolio-performance-bin quarto-cli-bin rar texlive-pgf-pie tiddlydesktop tor-browser tuxpaint tuxpaint-stamps vscodium-bin wakeonlan xfce4-multiload-ng-plugin zoom zotero-bin 
 
# Enjoy, bye ! 
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 

```
