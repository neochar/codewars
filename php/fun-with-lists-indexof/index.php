<?php

function index_of($head, $value, $index = 0)
{
    if (null === $head) {
        return -1;
    }
    if ($head->data === $value) {
        return $index;
    }
    return index_of($head->next, $value, $index + 1);
}
