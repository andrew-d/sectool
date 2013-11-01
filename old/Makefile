RUSTC=../rust/x86_64-apple-darwin/stage2/bin/rustc
RUST_FLAGS=

all: sec

sec: main.rs
	$(RUSTC) -o $@ $(RUST_FLAGS) $^

clean:
	$(RM) -rf sec *.dSYM
