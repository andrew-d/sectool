use std::hashmap::HashMap;


type CalllbackHash = HashMap<&'self str, &'self fn(_: &[&str])>;

struct OptionParser<'self> {
    priv banner: &'self str,
    priv cbs: CalllbackHash,
}


impl<'self> OptionParser<'self> {
    fn new(conf: &fn(_: &mut OptionParser)) -> OptionParser {
        let mut ret = OptionParser{banner: "", cbs: HashMap<&str, &fn(_: &[&str])>::new()};

        conf(&mut ret);

        ret
    }

    fn set_banner(&mut self, banner: &'self str) {
        self.banner = banner;
    }

    fn on(&mut self, arg: &'self str, cb: &fn(_: &[&str])) {

    }
}



#[test]
fn test_basic() {
    let op = do OptionParser::new |opts| {
        opts.set_banner("Usage: foo.rs [options]");
    };
}
