Summary:	Sonic-Rainbow is a graphical multi-media player for Linux.
Summary(pl):	Sonic-Rainbow jest graficznym odtwarzaczem plików multimedialnych.
Name:		sonic-rainbow
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/%{name}/%{name}-BETA-%{version}.tar.gz
# Source0-md5:	3554516ce325469cbcb62259c0e1bcf9
Source1:	%{name}.desktop
Source2:	%{name}.xpm
URL:		http://sonic-rainbow.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libao-devel >= 0.8
BuildRequires:	libcddb-devel >= 0.9.4
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	libvorbis-devel >= 1.0
BuildRequires:  libmad-devel >= 0.14
BuildRequires:  libid3tag-devel
BuildRequires:  xine-lib-devel > 1.0.0
BuildRequires:  audiofile-devel > 1:0.2.4
BuildRequires:	gtk+ >= 1.2.0
BuildRequires:	libao >= 0.8
BuildRequires:	libcddb >= 0.9.4
BuildRequires:	libogg >= 1.0
BuildRequires:	libvorbis >= 1.0
BuildRequires:  libmad >= 0.14
BuildRequires:  libid3tag
BuildRequires:  xine-lib > 1.0.0
BuildRequires:  audiofile > 0.2.4



BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sonic-Rainbow is a graphical multi-media player for Linux. It supports 
audio formats like mp3, wav and ogg , it also can play dvd and rip 
cd audio to mp3.

%description -l pl
Sonic-Rainbow jest graficznym odtwarzaczem plików multimedialnych.
Obs³uguje formaty muzyczne takie jak mp3, wav czy ogg. Potrafi tak¿e
odtwarzaæ filmy dvd oraz zrzucaæ pliki cd audio do formatu mp3.

%prep
%setup -q -n %{name}

%build
%{__aclocal}                                                                    
%{__autoconf}                                                                   
%{__automake}  
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT                                                          
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_applnkdir}/Multimedia}  
install src/sonic-rainbow $RPM_BUILD_ROOT%{_bindir}/sonic-rainbow
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia 
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)                                                     
%doc doc/Sonic-Rainbow.html AUTHORS NEWS README INSTALL
%attr(755,root,root) %{_bindir}/*                                               
%{_applnkdir}/Multimedia/%{name}.desktop                                        
%{_pixmapsdir}/sonic-rainbow.xpm 
