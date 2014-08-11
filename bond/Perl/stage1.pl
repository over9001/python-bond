### python-bond Perl interface setup
### NOTE: use ### for comments only, as this code is transformed into a single
###       line to be injected into the interpreter *without parsing*.
use strict;
use warnings;
use IO::Handle qw{};
use JSON qw{};

sub
{
  STDOUT->autoflush();
  print("STAGE2\n");

  my $line = <STDIN>;
  my $stage2 = JSON::decode_json($line);

  eval $stage2->{code};
  &{\&{$stage2->{func}}}(@{$stage2->{args}});
}->();