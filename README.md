# birthday-attacker
A small, simple program I wrote to try and cause a birthday attack on a hash

This is to mostly provide a skeleton of how this type of attack would work. This implemetnation uses character substitution of similar characters with each other.
For example, I looks very similar to l, so we try recursive cases to see which results in a longer match.

Be warned, it's performance intensive with this implementation, especially with higher character hit rates
