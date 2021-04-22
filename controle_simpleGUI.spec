# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['controle_simpleGUI.py'],
             pathex=['C:\\Users\\mathe\\Documents\\TV Digital\\remoteIR_software'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [ ('image_onoff.png', 'C:\\Users\\mathe\\Documents\\TV Digital\\image_onoff.png', 'DATA')]'
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='controle_simpleGUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
