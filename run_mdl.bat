@echo off
SET REPOSITORY=%~dp0
SET NEW_REPOSITORY=%REPOSITORY:\=/%
mdl "%NEW_REPOSITORY%docs/" -s "%NEW_REPOSITORY%.mdl_style.rb"