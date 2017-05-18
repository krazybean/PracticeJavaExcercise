package com.juan.controller;

import com.juan.domain.Advertiser;
import com.juan.domain.ObjectWithId;
import com.juan.service.AdvertiserService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import javax.inject.Inject;
import javax.inject.Named;

@RestController
@RequestMapping("/advertise")
public class AdvertiserRestController {
    private AdvertiserService advertiserService;

    private Logger logger=LoggerFactory.getLogger(AdvertiserRestController.class);

    @RequestMapping("")
    public String getBase(){
        return "Get Advertiser";
    }

    @Inject
    public AdvertiserRestController(@Named("advertiserService") AdvertiserService advertiserService){
        this.advertiserService=advertiserService;
    }

    @RequestMapping(value = "/{id}",method = RequestMethod.GET)
    @ResponseStatus(HttpStatus.OK)
    public Advertiser getAdvertiser(@PathVariable("id") Long id){
        System.out.println("Provider received request to get advertiser with id: " + id);
        logger.debug("Provider received request to get advertiser with id: " + id);
        return advertiserService.getAdvertiser(id);
    }

    @RequestMapping(method = RequestMethod.POST)
    @ResponseStatus(HttpStatus.CREATED)
    public ObjectWithId addAdvertiser(@RequestBody Advertiser advertiser){
        System.out.println("Advertiser to be created: " + advertiser);
        return new ObjectWithId(advertiserService.addAdvertiser(advertiser));
    }

    /*
    @RequestMapping(method = RequestMethod.DELETE)
    @ResponseStatus(HttpStatus.ACCEPTED)
    public ObjectWithId deleteAdvertiser(@RequestBody Advertiser advertiser){
        System.out.println("Advertiser to be deleted: " + advertiser);
        return new ObjectWithId(advertiserService.deleteAdvertiser(advertiser));
    }

    @RequestMapping(method = RequestMethod.PUT)
    @ResponseStatus(HttpStatus.ACCEPTED)
    public ObjectWithId updateAdvertiser(@RequestBody Advertiser advertiser){
        System.out.println("Advertiser to be updated: " + advertiser);
        return new ObjectWithId(advertiserService.updateAdvertiser(advertiser));
    }
    */
}