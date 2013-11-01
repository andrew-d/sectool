use std::os;
use std::hashmap::HashMap;


type Callback = ~fn(_: &[&str]);

struct OptionParser<'self> {
    priv banner: &'self str,
    priv cbs: HashMap<&'self str, Callback>,
}


impl<'self> OptionParser<'self> {
    fn new(conf: &fn(_: &mut OptionParser)) -> OptionParser {
        let hm = HashMap::<&str, Callback>::new();
        let mut ret = OptionParser{banner: "", cbs: hm};

        conf(&mut ret);

        ret
    }

    pub fn set_banner(&mut self, banner: &'self str) {
        self.banner = banner;
    }

    pub fn on(&mut self, arg: &'self str, cb: Callback) {
        self.cbs.insert(arg, cb);
    }

    pub fn parse(&self, args: &[~str]) {
        println!("Parse!")
    }
}



#[test]
fn test_basic() {
    let op = do OptionParser::new |opts| {
        opts.set_banner("Usage: foo.rs [options]");

        do opts.on("-v") |args| {
            println!("Verbose!")
        }
    };

    op.parse(os::args());
}
