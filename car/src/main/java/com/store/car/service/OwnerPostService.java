package com.store.car.service;

import com.store.car.dto.OwnerPostDTO;
import org.springframework.stereotype.Service;

@Service
public interface OwnerPostService {
    public void createOwnerPost(OwnerPostDTO ownerPostDTO);
}
