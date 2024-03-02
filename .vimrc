" VIM CONFIG FILES --- NOTE THAT THIS IS A WORK IN PROGRESS

" ============================================================
"                   BASIC CONFIGS
" ============================================================
set number
set shiftwidth=4
set tabstop=4
set noexpandtab
syntax on
filetype plugin indent on

" -------------------- Terminal Settings ---------------------
set splitbelow
set termguicolors

" ============================================================
"                   PLUGIN CONFIGS
" ============================================================

call plug#begin('~/.vim/plugged')

" --------------------------- Color Scheme -------------------
Plug 'sainnhe/everforest'

packadd! everforest

" Enable true color support if your terminal supports it
if has('termguicolors')
    set termguicolors
endif

set background=dark
let g:everforest_background = 'medium'
let g:everforest_better_performance = 1

colorscheme everforest

" Commented out plugins and schemes are not loaded
" Plug 'morhetz/gruvbox'
" colorscheme gruvbox
" colorscheme desert

" --------------------------- VimSpector  -------------------
Plug 'puremourning/vimspector'

call plug#end()

