<?php

function index_of($head, $value) {
    $i = 0;
    if (!isset($head->data)) {
        return -1; 
    }
    while ($head->data !== $value) {
        $i++;
        if (!isset($head->next)) {
            return -1;
        }
        $head = $head->next;
    }
    return $i;
}
