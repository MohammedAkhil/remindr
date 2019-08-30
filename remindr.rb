class Remaindr < Formula
  include Language::Python::Virtualenv

  desc "A CLI remainder"
  homepage ""
  url "https://github.com/MohammedAkhil/remindr/archive/0.1.tar.gz"
  sha256 "6039ac45d5b8f564e6c12ed06875fc03a39461e1ed15b3b266132ba9838cc0e0"
  head "https://github.com/MohammedAkhil/remindr.git"

  # TODO: If you're submitting an existing package, make sure you include your
  #       bottle block here.


  def install
    virtualenv_install_with_resources
  end

  # TODO: Add your package's tests here
end