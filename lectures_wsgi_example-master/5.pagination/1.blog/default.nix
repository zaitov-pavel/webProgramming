{ pkgs ? import <nixpkgs> {} }:

let
  php = pkgs.php;
  stdenv = pkgs.stdenv;
  python3 = pkgs.python35;
  pythonPackages = pkgs.python35Packages;

  paste3 = pythonPackages.buildPythonPackage rec {
    name = "paste-2.0.3";

    src = pkgs.fetchurl {
      url = mirror://pypi/P/Paste/Paste-2.0.3.tar.gz;
      sha256 = "062jk0nlxf6lb2wwj6zc20rlvrwsnikpkh90y0dn8cjch93s6ii3";
    };

    buildInputs = with pythonPackages; [ six ];

    doCheck = false; # some files required by the test seem to be missing

    meta = {
      description = "Tools for using a Web Server Gateway Interface stack";
      homepage = http://pythonpaste.org/;
    };
  };

  resolver = pythonPackages.buildPythonPackage rec {
    name = "resolver-0.2.1";

    src = pkgs.fetchurl {
      url = mirror://pypi/P/Paste/resolver-0.2.1.tar.gz;
      sha256 = "1hn709w0bpfg77s7pqrvfd2wlqnjmmm5vn8gzqid40jkahn15lvh";
    };

    doCheck = false; # some files required by the test seem to be missing
  };

  selector = pythonPackages.buildPythonPackage rec {
    name = "selector-0.10.1";

    src = pkgs.fetchurl {
      url = mirror://pypi/P/Paste/selector-0.10.1.tar.gz;
      sha256 = "03sq1dhll6k84s6acb57wrbc0x959s83bp2r5fysja5x6dwsiqrc";
    };

    buildInputs = with pythonPackages; [ resolver ];

    doCheck = false; # some files required by the test seem to be missing

    meta = {
      description = "This distribution provides WSGI middleware for “RESTful”
      mapping of URL paths to WSGI applications";
      homepage = "http://github.com/lukearno/selector/";
    };
  };

  wsgi-basic-auth = pythonPackages.buildPythonPackage rec {
    name = "wsgi-basic-auth-1.0.4";

    src = pkgs.fetchurl {
      url = mirror://pypi/P/Paste/wsgi-basic-auth-1.0.4.tar.gz;
      sha256 = "18dmkb0cazdpawnj4xp49ss70lq3mpnka7nfvg9y26ampfn6b5p5";
    };

    buildInputs = with pythonPackages; [ pythonPackages.webob ];

    doCheck = false; # some files required by the test seem to be missing
  };

  markupSafe = pythonPackages.buildPythonPackage rec {
    name = "MarkupSafe-0.9.3";

    src = pkgs.fetchurl {
      url = mirror://pypi/P/Paste/MarkupSafe-0.9.3.tar.gz;
      sha256 = "1grb90x0wn1r1wk5agqg631bb6ljs5c0q19i8dzvc0s4ca4ah93f";
    };

    doCheck = false; # some files required by the test seem to be missing
  };

  mako = pythonPackages.buildPythonPackage rec {
    name = "Mako-1.0.4";

    src = pkgs.fetchurl {
      url = mirror://pypi/P/Paste/Mako-1.0.4.tar.gz;
      sha256 = "0nchpw6akfcsg8w6irjlx0gyzadc123hv4g47sijgnqd9nz9vngy";
    };

    buildInputs = with pythonPackages; [ markupSafe ];

    doCheck = false; # some files required by the test seem to be missing
  };

  whitenoise = pythonPackages.buildPythonPackage rec {
    name = "whitenoise-1.0.4";

    src = pkgs.fetchurl {
      url = mirror://pypi/P/Paste/whitenoise-3.2.2.tar.gz;
      sha256 = "0h5lmsn3m4vif4g36bwcs7rzbby8glynlpcq3lncv8gpwgfpriz4";
    };

    doCheck = false; # some files required by the test seem to be missing
  };

  paginate = pythonPackages.buildPythonPackage rec {
    name = "paginate-0.5.4.tar.gz";

    src = pkgs.fetchurl {
      url = mirror://pypi/P/Paste/paginate-0.5.4.tar.gz;
      sha256 = "18x7sfpc0xhnxwz6cwhdwni010w09jgnfl85rm5zjfcdx7adzvq3";
    };

    doCheck = false; # some files required by the test seem to be missing
  };

in rec {
  pyEnv = stdenv.mkDerivation {
    name = "py-jinja";
    buildInputs = [ stdenv php python3 mako whitenoise paginate ] ++
                  [ pythonPackages.webob pythonPackages.ipdb ] ++
                  [ pythonPackages.jinja2 pythonPackages.six ] ++
                  [ paste3 selector resolver wsgi-basic-auth ];
  };
}
