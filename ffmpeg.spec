# OpenCV 3.X has an overlinking issue - unsuitable for core libraries
# Reported as https://github.com/opencv/opencv/issues/7001
%global _without_opencv   1

# Globals for git repository
%global commit0 0a155c57bd8eb92ccaf7f5857dc6ab276d235846
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}


Summary:    Digital VCR and streaming server
Name:       ffmpeg
Version:    4.0.2
Release:    8%{?dist}
%if 0%{?_with_amr:1}
License:    GPLv3+
%else
License:    GPLv2+
%endif
URL:        http://ffmpeg.org/
Source0:    https://git.ffmpeg.org/gitweb/ffmpeg.git/snapshot/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
ExclusiveArch:  %{arm}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:  bzip2-devel
%{?_with_faac:BuildRequires: faac-devel}
%{?_with_fdk_aac:BuildRequires: fdk-aac-devel}
%{?_with_flite:BuildRequires: flite-devel}
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
%{!?_without_frei0r:BuildRequires: frei0r-devel}
%{?_with_gme:BuildRequires: game-music-emu-devel}
BuildRequires:  gnutls-devel
BuildRequires:  gsm-devel
%{?_with_ilbc:BuildRequires: ilbc-devel}
BuildRequires:  lame-devel
%{!?_without_ladspa:BuildRequires: ladspa-devel}
BuildRequires:  libass-devel
%{?_with_bs2b:BuildRequires: libbs2b-devel}
%{?_with_caca:BuildRequires: libcaca-devel}
%{!?_without_cdio:BuildRequires: libcdio-paranoia-devel}
%{?_with_chromaprint:BuildRequires: libchromaprint-devel}
#libcrystalhd is currently broken
%{?_with_crystalhd:BuildRequires: libcrystalhd-devel}
%if 0%{?_with_ieee1394}
BuildRequires:  libavc1394-devel
BuildRequires:  libdc1394-devel
BuildRequires:  libiec61883-devel
%endif
BuildRequires:  libgcrypt-devel
BuildRequires:  libGL-devel
BuildRequires:  libmodplug-devel
%{?_with_rtmp:BuildRequires: librtmp-devel}
%{?_with_smb:BuildRequires: libsmbclient-devel}
%{?_with_ssh:BuildRequires: libssh-devel}
BuildRequires:  libtheora-devel
BuildRequires:  libv4l-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
%{?!_without_vpx:BuildRequires: libvpx-devel >= 0.9.1}
%{?_with_webp:BuildRequires: libwebp-devel}
%{?_with_netcdf:BuildRequires: netcdf-devel}
%{?_with_amr:BuildRequires: opencore-amr-devel vo-amrwbenc-devel}
%{!?_without_openal:BuildRequires: openal-soft-devel}
%if 0%{!?_without_opencl:1}
BuildRequires:  opencl-headers ocl-icd-devel
Recommends:     opencl-icd
%endif
%{!?_without_opencv:BuildRequires: opencv-devel}
BuildRequires:  openjpeg2-devel
BuildRequires:  openjpeg-devel
BuildRequires:  opus-devel
BuildRequires:  perl(Pod::Man)
%{?_with_rubberband:BuildRequires: rubberband-devel}
BuildRequires:  SDL2-devel
%{?_with_snappy:BuildRequires: snappy-devel}
BuildRequires:  soxr-devel
BuildRequires:  speex-devel
BuildRequires:  subversion
%{?_with_tesseract:BuildRequires: tesseract-devel}
BuildRequires:  texinfo
%{?_with_twolame:BuildRequires: twolame-devel}
%{?_with_wavpack:BuildRequires: wavpack-devel}
%{!?_without_x264:BuildRequires: x264-devel >= 0.152}
%{!?_without_xvid:BuildRequires: xvidcore-devel}
BuildRequires:  zlib-devel
%{?_with_zmq:BuildRequires: zeromq-devel}
%{?_with_zvbi:BuildRequires: zvbi-devel}
BuildRequires:  libxcb-devel libxcb
BuildRequires:  libdrm-devel
BuildRequires:  vid.stab-devel
BuildRequires:  zvbi-devel
BuildRequires:  alsa-lib-devel

### Rpi mmal / omx support
BuildRequires:  raspberrypi-vc-libs-devel
BuildRequires:  raspberrypi-vc-libs
BuildRequires:  raspberrypi-vc-static
BuildRequires:  libomxil-bellagio-devel


%description
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.


%package libs
Summary: Libraries for %{name}

%description libs
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains the libraries for %{name}


%package -n libavdevice
Summary: Special devices muxing/demuxing library

%description -n libavdevice
Libavdevice is a complementary library to libavf "libavformat". It provides
various "special" platform-specific muxers and demuxers, e.g. for grabbing
devices, audio capture and playback etc.


%package devel
Summary: Development package for %{name}
Requires: %{name}-libs%{_isa} = %{version}-%{release}
Requires: libavdevice%{_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: libxcb

%description devel
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains development files for %{name}


%global ff_configure \
./configure \\\
    --prefix=%{_prefix} \\\
    --bindir=%{_bindir} \\\
    --datadir=%{_datadir}/%{name} \\\
    --docdir=%{_docdir}/%{name} \\\
    --incdir=%{_includedir}/%{name} \\\
    --libdir=%{_libdir} \\\
    --mandir=%{_mandir} \\\
    --arch=%{_target_cpu} \\\
    --optflags="%{optflags}" \\\
    --extra-ldflags="%{?__global_ldflags}" \\\
    %{?_with_amr:--enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libvo-amrwbenc --enable-version3} \\\
    --enable-bzlib \\\
    --enable-libdrm \\\
    %{?_with_chromaprint:--enable-chromaprint} \\\
    %{!?_with_crystalhd:--disable-crystalhd} \\\
    --enable-fontconfig \\\
    %{!?_without_frei0r:--enable-frei0r} \\\
    --enable-gcrypt \\\
    %{?_with_gmp:--enable-gmp --enable-version3} \\\
    --enable-gnutls \\\
    %{!?_without_ladspa:--enable-ladspa} \\\
    --enable-libass \\\
    %{?_with_bs2b:--enable-libbs2b} \\\
    %{?_with_caca:--enable-libcaca} \\\
    %{!?_without_cdio:--enable-libcdio} \\\
    %{?_with_ieee1394:--enable-libdc1394 --enable-libiec61883} \\\
    %{?_with_faac:--enable-libfaac --enable-nonfree} \\\
    %{?_with_fdk_aac:--enable-libfdk-aac --enable-nonfree} \\\
    %{?_with_flite:--enable-libflite} \\\
    --enable-libfreetype \\\
    --enable-libfribidi \\\
    %{?_with_gme:--enable-libgme} \\\
    --enable-libgsm \\\
    %{?_with_ilbc:--enable-libilbc} \\\
    --enable-libmp3lame \\\
    %{?_with_netcdf:--enable-netcdf} \\\
    %{!?_without_openal:--enable-openal} \\\
    %{!?_without_opencl:--enable-opencl} \\\
    %{!?_without_opencv:--enable-libopencv} \\\
    --enable-libzvbi \\\
    --enable-libvidstab \\\
    %{!?_without_opengl:--enable-opengl} \\\
    --enable-libopenjpeg \\\
    --enable-libopus \\\
    %{?_with_rtmp:--enable-librtmp} \\\
    %{?_with_rubberband:--enable-librubberband} \\\
    %{?_with_smb:--enable-libsmbclient} \\\
    %{?_with_snappy:--enable-libsnappy} \\\
    --enable-libsoxr \\\
    --enable-libspeex \\\
    %{?_with_ssh:--enable-libssh} \\\
    %{?_with_tesseract:--enable-libtesseract} \\\
    --enable-libtheora \\\
    %{?_with_twolame:--enable-libtwolame} \\\
    --enable-libvorbis \\\
    --enable-libv4l2 \\\
    %{!?_without_vpx:--enable-libvpx} \\\
    %{?_with_webp:--enable-libwebp} \\\
    %{!?_without_x264:--enable-libx264} \\\
    %{!?_without_xvid:--enable-libxvid} \\\
    %{?_with_zmq:--enable-libzmq} \\\
    %{?_with_zvbi:--enable-libzvbi} \\\
    --enable-avfilter \\\
    --enable-avresample \\\
    --enable-postproc \\\
    --enable-pthreads \\\
    --disable-static \\\
    --enable-shared \\\
    --enable-gpl \\\
    --disable-debug \\\
    --disable-stripping


%prep
%autosetup -n %{name}-%{shortcommit0} -p1

# fix -O3 -g in host_cflags
sed -i "s|check_host_cflags -O3|check_host_cflags %{optflags}|" configure
mkdir -p _doc/examples
cp -pr doc/examples/{*.c,Makefile,README} _doc/examples/


%build
%{ff_configure}\
    --shlibdir=%{_libdir} \
    --disable-runtime-cpudetect --arch=arm \
%ifarch armv6hl
    --cpu=armv6 \
%else
    --enable-thumb \
%endif
%ifarch armv7hl
    --cpu=armv7-a \
    --enable-vfpv3 \
    --enable-neon \
%endif
    --enable-mmal \
    --enable-omx \
    --enable-omx-rpi \

%make_build V=1
make documentation V=1
make alltools V=1


%install
%make_install V=1
rm -r %{buildroot}%{_datadir}/%{name}/examples
install -pm755 tools/qt-faststart %{buildroot}%{_bindir}


%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post -n libavdevice -p /sbin/ldconfig

%postun -n libavdevice -p /sbin/ldconfig


%files
%doc COPYING.* CREDITS README.md
%{_bindir}/ffmpeg
%{_bindir}/ffplay
%{_bindir}/ffprobe
%{_bindir}/qt-faststart
%{_mandir}/man1/ffmpeg*.1*
%{_mandir}/man1/ffplay*.1*
%{_mandir}/man1/ffprobe*.1*
%{_datadir}/%{name}


%files libs
%{_libdir}/lib*.so.*
%exclude %{_libdir}/libavdevice.so.*
%{_mandir}/man3/lib*.3.gz
%exclude %{_mandir}/man3/libavdevice.3*


%files -n libavdevice
%{_libdir}/libavdevice.so.*
%{_mandir}/man3/libavdevice.3*


%files devel
%doc MAINTAINERS doc/APIchanges doc/*.txt
%doc _doc/examples
%doc %{_docdir}/%{name}/*.html
%{_includedir}/%{name}
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/lib*.so


%changelog

* Wed Jul 18 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.0.2-7
- Updated to 4.0.2-7

* Thu Jul 05 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.0.1-8
- Enabled libzvbi

* Sat Jun 16 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.0.1-7
- Updated to 4.0.1

* Sun May 27 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.0-9
- Automatic Mass Rebuild

* Fri Apr 20 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.0-7
- Updated to 4.0
- ffserver was removed
- Deprecate avfilter_link_get_channels(). Use av_buffersink_get_channels().

* Wed Mar 14 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.4.2-10
- Enabled missed alsa
- Updated to current commit in stable version

* Sat Feb 24 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.4.2-9
- Automatic Mass Rebuild

* Fri Feb 16 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.4.2-8
- Updated to stable release

* Tue Jan 30 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.4.2-7
- Updated to 3.4.2

* Mon Jan 29 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.4.1-11
- Updated to current commit in stable version

* Fri Jan 26 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.4.1-10
- Rebuilt for libcdio 2.0

* Tue Jan 16 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.4.1-9
- Rebuilt for libva 2.0

* Tue Dec 19 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.4.1-8
- Enabled vmaf

* Mon Dec 11 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.4.1-7
- Updated to 3.4.1

* Wed Dec 06 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.4-13
- Automatic Mass Rebuild

* Thu Nov 23 2017 David Va <davidva AT tutanota DOT com> 3.4-12
- Forces the buffers to be flushed after a drain has completed

* Tue Nov 21 2017 David Va <davidva AT tutanota DOT com> 3.4-11
- Patch for compatibility

* Fri Nov 17 2017 David Va <davidva AT tutanota DOT com> 3.4-10
- Enabled vid.stab

* Thu Nov 16 2017 David Va <davidva AT tutanota DOT com> 3.4-9
- Rebuilt

* Fri Nov 10 2017 David Va <davidva AT tutanota DOT com> 3.4-8
- Patch vc2enc_dwt: pad the temporary buffer by the slice size
- Patch forces the buffers to be flushed after a drain has completed

* Wed Oct 25 2017 David Va <davidva AT tutanota DOT com> 3.4-7
- Added support for libdrm, openh264, kvazaar, libmysofa and shine

* Mon Oct 16 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.4-1
- Updated to 3.4

* Thu Oct 05 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.3.4-4
- Automatic Mass Rebuild

* Sat Sep 30 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.3.4-3
- Automatic Mass Rebuild

* Wed Sep 13 2017 David Va <davidva AT tutanota DOT com> 3.3.4-2
- Updated to 3.3.4-2

* Fri Jul 28 2017 David Va <davidva AT tutanota DOT com> 3.3.3-3
- Updated to 3.3.3-3

* Thu Jun 15 2017 David Vásquez <davidva AT tutanota DOT com> 3.3.2-3
- Rebuilt for libbluray

* Fri Jun 09 2017 David Vásquez <davidva AT tutanota DOT com> 3.3.2-2
- Updated to 3.3.2-2

* Wed May 24 2017 David Vásquez <davidva AT tutanota DOT com> 3.3.1-2
- Updated to 3.3.1-2

* Tue Apr 25 2017 David Vásquez <davidva AT tutanota DOT com> - 3.3-2
- Rebuilt, for ffmpeg libs issues f24

* Tue Apr 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.3-1
- Automatic Mass Rebuild
- Updated to 3.3

* Sat Mar 18 2017 David Vásquez <davidva AT tutanota DOT com> - 3.2.4-4
- Rebuilt thanks to libbluray (sarcasm)

* Mon Feb 20 2017 David Vásquez <davidva AT tutanota DOT com> - 3.2.4-2
- Updated to 3.2.4-2
