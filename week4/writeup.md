# Week 4 Write-up

Tip: To preview this markdown file

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: Akmallullail Sya'ban \
SUNet ID: 2310817310010 \
Citations:

- `awesome-claude-agents` repository (for agent design patterns).
- `superclaude_framework` repository (for custom slash command logic).
- Materi Week 4: "Specs as the new source code" & "Frequent intentional compaction".

This assignment took me about **2** hours to do.

_(Implementation Note: Due to lack of access to the paid Anthropic API required for the Claude Code CLI, the execution of these automations was simulated using a hybrid approach with GitHub Copilot Pro in VS Code. The architecture and files (`CLAUDE.md` and `.claude/commands/test-format.md`) were built exactly to Claude Code specs as a proof of concept)._

## YOUR RESPONSES

### Automation #1: Context Guidance (`CLAUDE.md`)

a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)

> Inspirasi diambil dari repositori `awesome-claude-agents` dan materi "Coding Agent 101". Agen AI membutuhkan batasan yang jelas agar tidak berhalusinasi. `CLAUDE.md` dirancang sebagai "buku panduan manajerial" untuk menetapkan arsitektur dasar dan memaksakan alur kerja Test-Driven Development (TDD).

b. Design of each automation, including goals, inputs/outputs, steps

> - **Goals:** Memberikan agen pemahaman instan tentang arsitektur proyek (FastAPI, SQLite, Pytest) dan mewajibkan penulisan _unit test_ sebelum mengimplementasikan fitur.
> - **Inputs/Outputs:** Input berupa _prompt_ dari user (contoh: "Selesaikan Task 2"). Output berupa kode yang mematuhi standar _backend_ proyek.
> - **Steps:** (1) Agen otomatis membaca `CLAUDE.md` saat inisialisasi sesi. (2) Agen membaca `TASKS.md`. (3) Agen membuat _failing test_. (4) Agen menulis fitur utama untuk membuat tes menjadi hijau.

c. How to run it (exact commands), expected outputs, and rollback/safety notes

> - **How to run:** Buka Claude Code di dalam folder `week4/`. File ini akan otomatis dimuat sebagai _system prompt_. Berikan perintah: `"Tolong selesaikan Task 2: Add search endpoint"`.
> - **Expected outputs:** Agen menghasilkan file `test_notes.py` yang diperbarui dan `routers/notes.py` yang memiliki fitur pencarian.
> - **Rollback/safety notes:** Jika agen merusak logika _routing_ yang ada saat mencoba membuat fitur baru, pengguna dapat menjalankan `git restore .` atau mundur ke _commit_ sebelumnya.

d. Before vs. after (i.e. manual workflow vs. automated workflow)

> - **Before:** Saat meminta AI membuat fitur, AI sering membuat file baru yang tidak sesuai struktur proyek atau menggunakan _library_ yang tidak relevan karena kehilangan konteks. Developer harus terus-menerus mengingatkan AI tentang direktori proyek.
> - **After:** Dengan `CLAUDE.md`, AI langsung tahu di mana meletakkan _routers_ (`backend/app/routers`) dan _tests_ (`backend/tests/`). Alur kerja menjadi terstruktur secara otomatis tanpa perlu _prompting_ yang panjang dan berulang.

e. How you used the automation to enhance the starter application

> Saya memanfaatkannya untuk menyelesaikan **Task 2 (Add search endpoint for notes)**. Berdasarkan aturan `CLAUDE.md`, AI (yang disimulasikan via Copilot) pertama-tama diwajibkan menulis `test_search_notes` di `backend/tests/test_notes.py`. Setelah tes dibuat, barulah logika pencarian (menggunakan filter `contains` SQLAlchemy) diimplementasikan di `backend/app/routers/notes.py`.

### Automation #2: Custom Slash Command (`/test-format`)

a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)

> Inspirasi diambil dari `superclaude_framework` yang banyak menggunakan _slash commands_ untuk menyederhanakan tugas repetitif. Perintah `/test-format` dirancang untuk menggabungkan alur validasi _formatting_, _linting_, dan _testing_ ke dalam satu eksekusi agar AI dapat melakukan _self-correction_ jika terjadi error.

b. Design of each automation, including goals, inputs/outputs, steps

> - **Goals:** Menyederhanakan proses `make format` (black), `make lint` (ruff/flake8), dan `make test` (pytest) menjadi satu perintah sederhana yang dipicu dengan `/test-format`.
> - **Inputs/Outputs:** Input berupa ketikan `/test-format` di terminal agen. Output berupa terminal log (berhasil/gagal) dan perbaikan kode otomatis dari agen jika ada tes yang merah.
> - **Steps:** File `.claude/commands/test-format.md` menginstruksikan agen untuk menjalankan tiga perintah `make` secara berurutan. Jika ada yang gagal, agen diinstruksikan untuk tidak berhenti, melainkan langsung memperbaiki _source code_ yang bermasalah.

c. How to run it (exact commands), expected outputs, and rollback/safety notes

> - **How to run:** Di terminal Claude Code, ketik: `/test-format`. (Dalam simulasi ini, dijalankan manual melalui terminal VS Code dengan perintah `make check`).
> - **Expected outputs:** Semua _file_ diformat dengan benar, tidak ada peringatan _linting_, dan terminal menampilkan hasil `pytest` berwarna hijau.
> - **Rollback/safety notes:** Perintah ini hanya menggunakan _safe tools_ bawaan. Namun, jika _self-correction_ agen justru menghapus kode penting demi meloloskan linter, dapat dilakukan `git checkout -- <nama_file>` untuk membatalkan perubahan.

d. Before vs. after (i.e. manual workflow vs. automated workflow)

> - **Before:** Developer harus mengetik `make format`, menunggu selesai, mengetik `make lint`, melihat ada error di baris 42, membuka file, membenarkan indentasi manual, lalu menjalankan `make test`. Sangat repetitif dan memakan waktu.
> - **After:** Cukup ketik `/test-format`. Agen akan menjalankan ketiganya, membaca _stack trace_ error jika ada, membenarkan baris yang error secara otonom, lalu menjalankan ulang pengujian sampai sukses.

e. How you used the automation to enhance the starter application

> Setelah fitur _Search Endpoint_ untuk Task 2 selesai diimplementasikan, saya memicu otomatisasi ini (disimulasikan dengan `make check` di terminal). Otomatisasi ini merapikan indentasi kode yang baru saja saya tambahkan menggunakan `black`, memastikan tidak ada _import_ yang tidak terpakai menggunakan `ruff`, dan menjalankan _test suite_. Hasil akhirnya menunjukkan _test_ untuk `search_notes` berhasil lulus dengan aman.

### _(Optional) Automation #3_

_If you choose to build additional automations, feel free to detail them here!_

a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)

> N/A

b. Design of each automation, including goals, inputs/outputs, steps

> N/A

c. How to run it (exact commands), expected outputs, and rollback/safety notes

> N/A

d. Before vs. after (i.e. manual workflow vs. automated workflow)

> N/A

e. How you used the automation to enhance the starter application

> N/A
