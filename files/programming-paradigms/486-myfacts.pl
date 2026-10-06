likes(stefan,pop).
likes(stefan,classical).
likes(dino,folk).
likes(eugenia,folk).

likes(stefan,Music):-nottooloud(Music).
likes(stefan,Music):-likes(dino,Music),
    likes(eugenia,Music).

nottooloud(lullaby).
nottooloud(rock).


