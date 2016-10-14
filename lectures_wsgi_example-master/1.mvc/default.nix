{ pkgs ? import <nixpkgs> {} }:

let
  pythonPackages = pkgs.python35Packages;
  stdenv = pkgs.stdenv;
  python3 = pkgs.python35;

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

    buildInputs = with pythonPackages; [];

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
in rec {
  pyEnv = stdenv.mkDerivation {
    name = "py-paste";
    buildInputs = [ stdenv python3 paste3 ]
      ++ [ resolver selector wsgi-basic-auth ]
      ++ [ pythonPackages.webob pythonPackages.ipdb ];
  };
}
