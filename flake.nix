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
				nodejs
				python311
                pyright
                isort
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
				python311Packages.black
				python311Packages.flake8
				python311Packages.sentinel
				python311Packages.python-lsp-server
				python311Packages.virtualenv
				python311Packages.pyflakes  # Linter Pyflakes
                python311Packages.isort
# # Extra Emacs Packages
# 				emacsPackages.web-mode
# 				emacsPackages.lsp-mode
# 				emacsPackages.emmet-mode
# 				emacsPackages.flycheck
# 				emacsPackages.lsp-ui
# 				prettierd
# 				emacs
				];                
				shellHook = ''                                                           
					echo "Welcome to the Day Planner and Investment Tracker environment!"                    
					'';                                                                                      
				};                                                                                         
				}
				);
}
