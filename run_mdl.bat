@echo off
SET REPOSITORY=%~dp0
SET NEW_REPOSITORY=%REPOSITORY:\=/%
mdl "%NEW_REPOSITORY%docs/process_manual" -s "%NEW_REPOSITORY%.mdl_style.rb"