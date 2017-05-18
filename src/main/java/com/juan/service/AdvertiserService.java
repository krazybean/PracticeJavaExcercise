package com.juan.service;

import com.juan.domain.Advertiser;

public interface AdvertiserService{
    public Advertiser getAdvertiser(long id);

    public long addAdvertiser(Advertiser advertiser);

    public long getAdvertiserCount();

    /*
    public long deleteAdvertiser(Advertiser advertiser);

    public long updateAdvertiser(Advertiser advertiser);
    */
}