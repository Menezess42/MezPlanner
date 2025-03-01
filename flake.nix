{
    description = "Day Planner and Investment Tracker";

    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
        flake-utils.url = "github:numtide/flake-utils";
    };

    outputs = { self, nixpkgs, flake-utils }:
        flake-utils.lib.eachDefaultSystem (system:
                let
                pkgs = import nixpkgs { inherit system; };
#enableIDE = true;
#idePackages = if enableIDE then import ./ide-packages.nix {inherit pkgs; } else [];
                in {
                devShell = pkgs.mkShell {
                name = "day-planner-env";
                buildInputs = with pkgs; [
                curl
                direnv
                sqlite
                # JS 4 the project and IDE like features on neovim
                nodejs
                eslint
                pkgs.vscode-langservers-extracted
                # Python 4 the project and IDE Like features on neovim
                python311
                pyright
                python311Packages.pip
                python311Packages.pandas
                python311Packages.openpyxl
                python311Packages.matplotlib
                python311Packages.flask
                python311Packages.sqlalchemy
                python311Packages.flask-sqlalchemy
                python311Packages.flask-migrate
                python311Packages.flask-login
                python311Packages.flask-bcrypt
                python311Packages.pytest
                python311Packages.pytest-flask
                python311Packages.jedi
                python311Packages.jedi-language-server
                python311Packages.black
                python311Packages.flake8
                python311Packages.sentinel
                python311Packages.python-lsp-server
                python311Packages.virtualenv
                python311Packages.pyflakes  # Linter Pyflakes
                python311Packages.isort
                ];                
                shellHook = ''                                                           
                    echo "Welcome to the Day Planner and Investment Tracker environment!"                    
                    '';                                                                                      
                };                                                                                         
                }
                );
}
