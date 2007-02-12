Summary:	Sonic-Rainbow - a graphical multi-media player for Linux
Summary(pl.UTF-8):	Sonic-Rainbow - graficzny odtwarzacz plików multimedialnych
Name:		sonic-rainbow
Version:	0.7.2.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/sonic-rainbow/%{name}-ALPHA-%{version}.tar.gz
# Source0-md5:	ee0bf129b9943a06acc66b7b155af0b2
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-cddb.patch
URL:		http://sonic-rainbow.sourceforge.net/
BuildRequires:	audiofile-devel > 1:0.2.4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	id3lib-devel
BuildRequires:	libao-devel >= 0.8
BuildRequires:	libcddb-devel >= 0.9.4
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel >= 0.14
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	xine-lib-devel > 1.0.0
Requires:	audiofile > 0.2.4
Requires:	gtk+ >= 1.2.0
Requires:	libao >= 0.8
Requires:	libcddb >= 0.9.4
Requires:	libogg >= 1.0
Requires:	libmad >= 0.14
Requires:	libvorbis >= 1.0
Requires:	xine-lib > 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sonic-Rainbow is a graphical multi-media player for Linux. It supports
audio formats like MP3, WAV and Ogg , it also can play dvd and rip cd
audio to MP3.

%description -l pl.UTF-8
Sonic-Rainbow jest graficznym odtwarzaczem plików multimedialnych.
Obsługuje formaty muzyczne takie jak MP3, WAV czy Ogg. Potrafi także
odtwarzać filmy dvd oraz zrzucać pliki cd audio do formatu MP3.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}}

install src/sonic-rainbow $RPM_BUILD_ROOT%{_bindir}/sonic-rainbow
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/Sonic-Rainbow.html AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/sonic-rainbow.xpm
