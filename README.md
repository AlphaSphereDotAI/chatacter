# Graduation Project
This is a graduation project for a 6-member team at Cairo University. For a more detailed report, click [here](https://docs.google.com/document/d/1AqPmSc7sS0sIT5c1Txxk98LEKcT2caWGn9AnyRQPEmo/edit?usp=sharing)
## Ideas
- Frame Rate Enhancer
- Handwritten BCI Recognition
- Chat with Characters in History
- Glass with Computer Vision

### Frame Rate Enhancer
After using the RIFE Model, it enhances 5 FPS video to 20 FPS.

![5 FPS video to 20 FPS](https://github.com/MH0386/graduation_project/assets/77013511/37a4e785-74a5-405a-adb9-a19f8a90f2c7)


<details>
<summary>In Terminal:</summary>
 
 ```
loaded v3.x HD model.
 v.mp4, 150.0 frames in total, 5.0 FPS to 20.0 FPS
 The audio will be merged after the interpolation process
  99%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▉ | 149/150.0 [00:29<00:00,  5.02it/s]
 ffmpeg version 4.4.2-0ubuntu0.22.04.1 Copyright (c) 2000-2021 The FFmpeg developers
   built with gcc 11 (Ubuntu 11.2.0-19ubuntu1)
   configuration: --prefix=/usr --extra-version=0ubuntu0.22.04.1 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --arch=amd64 --enable-gpl --disable-stripping --enable-gnutls --enable-ladspa --enable-libaom --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libcodec2 --enable-libdav1d --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libjack --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librabbitmq --enable-librubberband --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libsrt --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzimg --enable-libzmq --enable-libzvbi --enable-lv2 --enable-omx --enable-openal --enable-opencl --enable-opengl --enable-sdl2 --enable-pocketsphinx --enable-librsvg --enable-libmfx --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libx264 --enable-shared
   libavutil      56. 70.100 / 56. 70.100
   libavcodec     58.134.100 / 58.134.100
   libavformat    58. 76.100 / 58. 76.100
   libavdevice    58. 13.100 / 58. 13.100
   libavfilter     7.110.100 /  7.110.100
   libswscale      5.  9.100 /  5.  9.100
   libswresample   3.  9.100 /  3.  9.100
   libpostproc    55.  9.100 / 55.  9.100
 Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'v.mp4':
   Metadata:
     major_brand     : isom
     minor_version   : 512
     compatible_brands: isomiso2avc1mp41
     encoder         : Lavf59.27.100
   Duration: 00:00:30.02, start: 0.000000, bitrate: 3876 kb/s
   Stream #0:0(und): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 2 kb/s (default)
     Metadata:
       handler_name    : SoundHandler
       vendor_id       : [0][0][0][0]
   Stream #0:1(und): Video: h264 (High) (avc1 / 0x31637661), yuvj420p(pc, bt709), 1280x720 [SAR 1:1 DAR 16:9], 3873 kb/s, 5 fps, 5 tbr, 10240 tbn, 10 tbc (default)
     Metadata:
       handler_name    : VideoHandler
       vendor_id       : [0][0][0][0]
 Output #0, matroska, to './temp/audio.mkv':
   Metadata:
     major_brand     : isom
     minor_version   : 512
     compatible_brands: isomiso2avc1mp41
     encoder         : Lavf58.76.100
   Stream #0:0(und): Audio: aac (LC) ([255][0][0][0] / 0x00FF), 48000 Hz, stereo, fltp, 2 kb/s (default)
     Metadata:
       handler_name    : SoundHandler
       vendor_id       : [0][0][0][0]
 Stream mapping:
   Stream #0:0 -> #0:0 (copy)
 Press [q] to stop, [?] for help
 size=      18kB time=00:00:29.99 bitrate=   4.8kbits/s speed= 703x
 video:0kB audio:8kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 109.707603%
 ffmpeg version 4.4.2-0ubuntu0.22.04.1 Copyright (c) 2000-2021 The FFmpeg developers
   built with gcc 11 (Ubuntu 11.2.0-19ubuntu1)
   configuration: --prefix=/usr --extra-version=0ubuntu0.22.04.1 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --arch=amd64 --enable-gpl --disable-stripping --enable-gnutls --enable-ladspa --enable-libaom --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libcodec2 --enable-libdav1d --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libjack --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librabbitmq --enable-librubberband --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libsrt --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzimg --enable-libzmq --enable-libzvbi --enable-lv2 --enable-omx --enable-openal --enable-opencl --enable-opengl --enable-sdl2 --enable-pocketsphinx --enable-librsvg --enable-libmfx --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libx264 --enable-shared
   libavutil      56. 70.100 / 56. 70.100
   libavcodec     58.134.100 / 58.134.100
   libavformat    58. 76.100 / 58. 76.100
   libavdevice    58. 13.100 / 58. 13.100
   libavfilter     7.110.100 /  7.110.100
   libswscale      5.  9.100 /  5.  9.100
   libswresample   3.  9.100 /  3.  9.100
   libpostproc    55.  9.100 / 55.  9.100
 Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'v_4X_20fps_noaudio.mp4':
   Metadata:
     major_brand     : isom
     minor_version   : 512
     compatible_brands: isomiso2mp41
     encoder         : Lavf59.27.100
   Duration: 00:00:29.85, start: 0.000000, bitrate: 1705 kb/s
   Stream #0:0(und): Video: mpeg4 (Simple Profile) (mp4v / 0x7634706D), yuv420p, 1280x720 [SAR 1:1 DAR 16:9], 1704 kb/s, 20 fps, 20 tbr, 10240 tbn, 20 tbc (default)
     Metadata:
       handler_name    : VideoHandler
       vendor_id       : [0][0][0][0]
 Input #1, matroska,webm, from './temp/audio.mkv':
   Metadata:
     COMPATIBLE_BRANDS: isomiso2avc1mp41
     MAJOR_BRAND     : isom
     MINOR_VERSION   : 512
     ENCODER         : Lavf58.76.100
   Duration: 00:00:30.04, start: 0.000000, bitrate: 4 kb/s
   Stream #1:0: Audio: aac (LC), 48000 Hz, stereo, fltp (default)
     Metadata:
       HANDLER_NAME    : SoundHandler
       VENDOR_ID       : [0][0][0][0]
       DURATION        : 00:00:30.037000000
 Output #0, mp4, to 'v_4X_20fps.mp4':
   Metadata:
     major_brand     : isom
     minor_version   : 512
     compatible_brands: isomiso2mp41
     encoder         : Lavf58.76.100
   Stream #0:0(und): Video: mpeg4 (Simple Profile) (mp4v / 0x7634706D), yuv420p, 1280x720 [SAR 1:1 DAR 16:9], q=2-31, 1704 kb/s, 20 fps, 20 tbr, 10240 tbn, 10240 tbc (default)
     Metadata:
       handler_name    : VideoHandler
       vendor_id       : [0][0][0][0]
   Stream #0:1: Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp (default)
     Metadata:
       HANDLER_NAME    : SoundHandler
       VENDOR_ID       : [0][0][0][0]
       DURATION        : 00:00:30.037000000
 Stream mapping:
   Stream #0:0 -> #0:0 (copy)
   Stream #1:0 -> #0:1 (copy)
 Press [q] to stop, [?] for help
 frame=  597 fps=0.0 q=-1.0 Lsize=    6238kB time=00:00:30.01 bitrate=1702.5kbits/s speed= 479x
 video:6211kB audio:8kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.304409%
 ```

</details>
