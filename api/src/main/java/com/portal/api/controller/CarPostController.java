package com.portal.api.controller;

import com.portal.api.dto.CarPostDTO;
import com.portal.api.message.KafkaProducerMessager;
import com.portal.api.service.CarPostStoreService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/car")
public class CarPostController {

    private final Logger LOG = LoggerFactory.getLogger(CarPostController.class);

    @Autowired
    private CarPostStoreService carPostService;

    @Autowired
    private KafkaProducerMessager kafkaProducerMessager;

    @PostMapping("/post")
    public ResponseEntity<CarPostDTO> createCarForSale(@RequestBody CarPostDTO carPostDTO){

        LOG.info("USING EVENTS/MESSAGES KAFKA - Producer Car Post information: {}", carPostDTO);
        kafkaProducerMessager.sendMessage(carPostDTO);
        return new ResponseEntity<>(HttpStatus.OK);
    }

    @GetMapping("/posts")
    public ResponseEntity<List<CarPostDTO>> getCarSales(){
        return ResponseEntity.status(HttpStatus.FOUND).body(carPostService.getCarsForSales());
    }

    @PutMapping("/{id}")
    public ResponseEntity<CarPostDTO> changeCarSales(@RequestBody CarPostDTO carPostDTO, @PathVariable("id") String id){
        carPostService.changeCarForSale(carPostDTO,id);
        return ResponseEntity.ok().build();
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<CarPostDTO> deleteCarSale(@PathVariable("id") String id){
        carPostService.removeCarForSale(id);
        return ResponseEntity.ok().build();
    }
}
