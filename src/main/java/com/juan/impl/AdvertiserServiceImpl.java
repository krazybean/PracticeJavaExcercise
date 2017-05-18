package com.juan.impl;

import com.juan.domain.Advertiser;
import com.juan.service.AdvertiserService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.inject.Named;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

@Named("advertiserService")
public abstract class AdvertiserServiceImpl implements AdvertiserService{

    public static Logger logger = LoggerFactory.getLogger(AdvertiserServiceImpl.class);
    public AtomicInteger atomicInterger = new AtomicInteger(0);

    public AdvertiserServiceImpl(){
        init();
    }

    private List<Advertiser> advertisers = new ArrayList<>();

    private void init(){
        addAdvertiser("TestAdvertiser1", "ContactInfo1", 1000);
        addAdvertiser("TestAdvertiser2", "ContactInfo2", 5000);
    }

    public Advertiser getAdvertiser(long id){
        logger.info("Retrieving id {}", id);
        for (Advertiser advertiser: advertisers){
            if (advertiser.getId()==id){
                return advertiser;
            }
        }
        return null;
    }

    public long addAdvertiser(Advertiser advertiser){
        int idTodSet=atomicInterger.getAndIncrement();
        advertiser.setId(idTodSet);
        advertisers.add(advertiser);
        return idTodSet;
    }

    public long addAdvertiser(String Name, String Contact, int CreditLimit){
        Advertiser advertiser = new Advertiser(-1, Name, Contact, CreditLimit);
        return addAdvertiser(advertiser);
    }

    /*
    public long deleteAdvertiser(Advertiser advertiser){
        int idTodSet=atomicInterger.getAndDecrement();
        return deleteAdvertiser(advertiser);
    }

    public long updateAdvertiser(Advertiser advertiser){
        int idTodSet=atomicInterger.get();
        return updateAdvertiser(advertiser);
    }
    */
    public long getAdvertiserCount(){
        return advertisers.size();
    }
}