<?php

class Node
{
    public $data, $next;
    public function __construct($data, $next = null)
    {
        $this->data = $data;
        $this->next = $next;
    }
}
