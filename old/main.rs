extern mod extra;

use std::os;
use std::rt::io::{stdin, stdout, Reader, Writer};
use std::rt::io::mem::MemReader;
use std::option::{Option, Some, None};
use std::str::{from_utf8};
use extra::url::{encode, decode};


struct UrlEncoder {
    priv quotes: bool,
}

impl UrlEncoder {
    pub fn new() -> UrlEncoder {
        UrlEncoder{quotes: false}
    }

    pub fn process<'a>(&self, buff: &[u8]) -> ~[u8] {
        debug!("Processing vector of length: {}", buff.len());
        let encoded = encode(from_utf8(buff));
        debug!("Encoded = {}", encoded);
        encoded.as_bytes().to_owned()
    }
}


fn main() {
    let args = os::args();

    if args.len() < 2 {
        fail!("No arguments given!");
    }

    // Get input.
    let mut inp_source = ~"-";
    if args.len() >= 3 && args[2] != inp_source {
        inp_source = args[2].clone();
    }

    let mut input: ~Reader = match inp_source {
        ~"-"    => ~stdin() as ~Reader,
        s       => ~MemReader::new(s.as_bytes().to_owned()) as ~Reader,
    };

    let mut stream = match args[1] {
        ~"urlencode" => {
            debug!("Url encode");
            UrlEncoder::new()
        },
        // ~"urldecode" => {
        //     println!("Url decode");
        //     2
        // },
        bad => fail!("Bad command {}", bad),
    };

    let mut buff = [0, ..100];
    let mut out = stdout();
    loop {
        let output = match input.read(buff) {
            Some(amount) => {
                stream.process(buff.slice_to(amount))
            },
            None         => break,
        };

        out.write(output);
    }
}
