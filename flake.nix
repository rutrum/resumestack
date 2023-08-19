{
  description = "resume-stack flake";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {

    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [ 
        just
        watchexec
        (python3.withPackages (ps: with ps; [ toml ]))
        texlive.combined.scheme-full
      ];
    };

  };
}
